import numpy as np

img = PIL.Image.open('image_path')
updated_img = np.array(img)

# horizontal flip
horizontal_flip = updated_img[:, ::-1]
# vertical flip
vertical_flip = updated_img[::-1]

# How to identify R-G-B channels
# Image URL: https://www.educba.com/rgb-color-model/
img = PIL.Image.open('image_path')

img = np.array(img)

# Fetching R channel
img[:, :, 0]
# Fetching G channel
img[:, :, 1]
# Fetching B channel
img[:, :, 2]


# create base image for validation of arrays

# First will create white square of size 100 x 100
first = np.full((100,100), fill_value=255).astype(np.uint8)
# First will create black square of size 100 x 100
second = np.full((100,100), fill_value=0).astype(np.uint8)
# First will create grey square of size 5 x 100
grey = np.full((5,100), fill_value=125).astype(np.uint8)

# add same or different colors in horizontal fashion
third = np.concatenate((first, second, first), axis=1)
third_ = np.concatenate((grey_, third, grey_, third, grey_, third, grey_), axis=0)