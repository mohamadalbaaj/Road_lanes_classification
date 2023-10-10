# Road_lanes_classification
Road_lanes_classification_from_pointclouds_using_machine_learning
## Prerequisites
- Python version 3.10
- jupter notebook
note: To ensure seamless integration, please modify the paths as per your specific dataset storage location
### Required libraries
- pip install pandas
- pip install numpy
- pip install python-time
- pip install os-sys
- pip install scikit-learn
- pip install matplotlib
- pip install tensorflow
- pip install torch
- pip install torchvision
- pip install torchstat
- pip install Pillow
- pip install opencv-python
- pip install tqdm
- pip install seaborn
## Approaches used
Approach 1 decision tree
Approach 2 pointcloud2image
Approach 3 point net
Note: Approach 2 was employed due to the nature of the dataset, which consists of road lane segments. The primary focus lies in extracting valuable insights from the surface characteristics.
## Dataset
Road lane segments as .npy

distributed into 6 clasess
2lanes
3lanes
crossing
split4lanes
split6lanes
transition

with 22 features
0  local x
1  local y
2  local z
3  red values
4  green values
5  blue values
6  global x
7  global y
8  global z
9  intensity
10 number of lidar returns
11 planarity
12 linearity
13 sphericity
14 verticality
15 mean intensity in 0.3m increments along y 
16 mean intensity in 1.5m increments along y 
17 mean intensity in 0.3m increments along x 
18 mean intensity in 1.5m increments along x 
19 edge area 
20 grid increment index 0.3m resolution
21 intensity principal gradient positions

Note: I provided one example of the dataset 


