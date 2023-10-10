Road_lanes_classification_pointclouds_machine_learning

Prerequisites
Python version 3.10
jupter notebook
note: To ensure seamless integration, please modify the paths as per your specific dataset storage location

Required libraries
Use the following command to install the necessary libraries:

pip install pandas
pip install numpy
pip install python-time
pip install os-sys
pip install scikit-learn
pip install matplotlib
pip install tensorflow
pip install torch
pip install torchvision
pip install torchstat
pip install Pillow
pip install opencv-python
pip install tqdm
pip install seaborn

Approaches used
approach 1 decision tree
approach 2 pointcloud2image
approach 3 point net

note: Approach 2 was employed due to the nature of the dataset, which consists of road lane segments. The primary focus lies in extracting valuable insights from the surface characteristics.

dataset 1425 road lane segments as .npy

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

note: I provided one example of the dataset 



