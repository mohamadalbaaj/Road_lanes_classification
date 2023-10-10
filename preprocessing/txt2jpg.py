import numpy as np
import cv2
import os

def local_file(file_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(script_dir, 'dataset', file_name)
    return data_file_path

def read_point_cloud(file_path):
    data = np.loadtxt(file_path, delimiter=',', usecols=range(22))  # Load all 22 columns
    return data

def create_grayscale_color(data):
    # Extract red, green, and blue values from columns 3, 4, and 5
    red_values = data[:, 3]
    green_values = data[:, 4]
    blue_values = data[:, 5]

    # Create a grayscale image using average of red, green, and blue values
    grayscale_color = (red_values + green_values + blue_values) / 3
    
    return grayscale_color

    # normalize the intensity from range (0 to 65535) to (0 to 255)
def normalize_intensity(data):
    intensity_column = data[:, 9]
    normalized_intensity = (intensity_column / 65535.0) * 255
    return normalized_intensity

def intensity_principal_gradient_positions(data):
    intensity_principle = data[:, 21]

    # normalize the intensity principal gradient positions from range (-1 to 1,5) to (0 to 255)
    intensity_principle_column = ((intensity_principle + 0.5)/2) * 255

    return intensity_principle_column

def create_occupancy_grid_with_color_and_intensity(data, resolution, grayscale_color, normalized_intensity, intensity_principle_column):
    # Extract x and y values from columns 0 and 1
    x_values = data[:, 0]
    y_values = data[:, 1]
    
    # Determine grid size based on min and max x, y values
    min_x, max_x = np.min(x_values), np.max(x_values)
    min_y, max_y = np.min(y_values), np.max(y_values)
    
    grid_width = int((max_x - min_x) / resolution) + 1
    grid_height = int((max_y - min_y) / resolution) + 1
    
    # Initialize combined grid (occupancy + grayscale color + intensity channels)
    combined_grid = np.zeros((grid_height, grid_width, 3), dtype=np.float32)
    
    # Populate the combined grid
    for x, y, gray_value, intensity_value, intensity_principle_value in zip(x_values, y_values, grayscale_color, normalized_intensity, intensity_principle_column):
        grid_x = int((x - min_x) / resolution)
        grid_y = int((y - min_y) / resolution)
        if 0 <= grid_x < grid_width and 0 <= grid_y < grid_height:
            combined_grid[grid_y, grid_x, 0] = intensity_value  # Assign intensity value
            combined_grid[grid_y, grid_x, 1] = gray_value  # Assign grayscale color
            combined_grid[grid_y, grid_x, 2] = intensity_principle_value  # Assign intensity_principle_value
    
    return combined_grid


def save_occupancy_grid_as_jpg(combined_grid, output_path):

    # Flip the image vertically
    occupancy_grid_flipped = cv2.flip(combined_grid, 0)

    cv2.imwrite(output_path, occupancy_grid_flipped)

def main():
    folder_path = local_file("transition_txt")

    output_folder = "transition_jpg"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):
            data = read_point_cloud(file_path)
            grayscale_color = create_grayscale_color(data)
            normalized_intensity_values = normalize_intensity(data)
            normalized_inten_principle = intensity_principal_gradient_positions(data)
            resolution = 0.2
            occupancy_grid_with_intensity = create_occupancy_grid_with_color_and_intensity(data, resolution, grayscale_color, normalized_intensity_values, normalized_inten_principle)
            file_base = os.path.splitext(file_name)[0]
            output_path = os.path.join(output_folder, file_base + ".jpg")
            save_occupancy_grid_as_jpg(occupancy_grid_with_intensity, output_path)

if __name__ == "__main__":
    main()
