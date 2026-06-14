# coding: utf-8

# In[ ]:
import os

import tensorflow as tf

import keras
from keras.engine.saving import load_model
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Activation, Dropout, Flatten

from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np

#------------------------------
# sess = tf.Session()
# keras.backend.set_session(sess)
#------------------------------
#variables
num_classes =6
batch_size = 30
epochs = 50
#------------------------------

import os, cv2, keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.engine.saving import load_model
# manipulate with numpy,load with panda
import numpy as np
# import pandas as pd

# data visualization
import cv2
import matplotlib
import matplotlib.pyplot as plt
# import seaborn as sns

# get_ipython().run_line_magic('matplotlib', 'inline')


# Data Import
def read_dataset(path):
    data_list = []
    label_list = []

    file_path = os.path.join(path)
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
    data_list.append(res)
    # label = dirPath.split('/')[-1]

    return (np.asarray(data_list, dtype=np.float32))



def predict_shape(path):
    c=["Long,Narrow Triangle","Round Triangle","Invalid"]
    model = load_model(r"C:\Users\user\Desktop\myproject final1\myproject\myapp\modelshape.h5")  # load weights
    f=read_dataset(path)
    x_train = np.array(f, 'float32')

    x_train /= 255  # normalize inputs between [0, 1]
    x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
    yp = model.predict_classes(x_train, verbose=0)
    return c[yp[0]]

# print(predict(r"C:\PycharmProjects\PycharmProjects\myproject\media\bba2.jpeg"))