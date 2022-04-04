import numpy as np

# create 2 numpy array with values ranges between 0 and 1
# 2 arrays with 10 elements in each
x_numpy = np.random.rand(10000000)
y_numpy = np.random.rand(10000000)

z_numpy = np.absolute(x_numpy - y_numpy)