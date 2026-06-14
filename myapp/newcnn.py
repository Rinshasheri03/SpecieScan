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
batch_size = 60
epochs = 65
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

import cv2
import numpy as np
import random
# Data Import



def rotate_image(img, angle_range=40):
    angle = random.uniform(-angle_range, angle_range)
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(img, rotation_matrix, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
    return rotated


# Shear
def shear_image(img, shear_range=0.2):
    h, w = img.shape[:2]
    shear_factor = random.uniform(-shear_range, shear_range)
    M = np.array([[1, shear_factor, 0], [0, 1, 0]], dtype=np.float32)
    sheared = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT_101)
    return sheared


# Zoom
def zoom_image(img, zoom_range=0.2):
    h, w = img.shape[:2]
    zoom_factor = 1 + random.uniform(-zoom_range, zoom_range)
    new_h, new_w = int(h * zoom_factor), int(w * zoom_factor)
    zoomed = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    if zoom_factor > 1:  # Crop center
        crop_h = (new_h - h) // 2
        crop_w = (new_w - w) // 2
        zoomed = zoomed[crop_h:crop_h + h, crop_w:crop_w + w]
    else:  # Pad with border reflection
        pad_h = (h - new_h) // 2
        pad_w = (w - new_w) // 2
        zoomed = cv2.copyMakeBorder(zoomed, pad_h, h - new_h - pad_h, pad_w, w - new_w - pad_w, cv2.BORDER_REFLECT_101)
    return zoomed


# Horizontal Flip
def horizontal_flip(img):
    if random.random() < 0.5:
        return cv2.flip(img, 1)
    return img


# Brightness Adjustment
def adjust_brightness(img, brightness_range=(0.8, 1.2)):
    factor = random.uniform(brightness_range[0], brightness_range[1])
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype=np.float32)
    hsv[..., 2] *= factor
    hsv[..., 2] = np.clip(hsv[..., 2], 0, 255)
    adjusted = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    return adjusted


# Apply transformations


# Data Import
def read_dataset():
    data_list = []
    label_list = []
    my_list = os.listdir(r'C:\Users\user\Pictures\species')
    print(my_list)
    for pos,pa in enumerate(my_list):

        print(pa,"==================")
        for root, dirs, files in os.walk(r'C:\Users\user\Pictures\species\\' + pa):

         for f in files:
            file_path = os.path.join(r'C:\Users\user\Pictures\species\\' + pa, f)
            img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)


            res = cv2.resize(img, (48, 48), interpolation=cv2.INTER_CUBIC)
            data_list.append(res)
            label_list.append(pos)


            img= cv2.imread(file_path)




            # label_list.remove("./training")
    return (np.asarray(data_list, dtype=np.float32), np.asarray(label_list))

    print("=====================",label_list)


from sklearn.model_selection import train_test_split
# load dataset
x_dataset, y_dataset = read_dataset()
X_train, X_test, y_train, y_test = train_test_split(x_dataset, y_dataset, test_size=0.2, random_state=0)

y_train1=[]
for i in y_train:
    emotion = keras.utils.to_categorical(i, num_classes)

    y_train1.append(emotion)

y_train=y_train1
x_train = np.array(X_train, 'float32')
y_train = np.array(y_train, 'float32')
x_test = np.array(X_test, 'float32')
y_test = np.array(y_test, 'float32')

x_train /= 255  # normalize inputs between [0, 1]
x_test /= 255
print("x_train.shape",x_train.shape)
x_train = x_train.reshape(x_train.shape[0], 48, 48, 1)
x_train = x_train.astype('float32')
x_test = x_test.reshape(x_test.shape[0], 48, 48, 1)
x_test = x_test.astype('float32')

print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
# ------------------------------
# construct CNN structure

model = Sequential()

# 1st convolution layer
model.add(Conv2D(64, (5, 5), activation='relu', input_shape=(48, 48, 1)))
model.add(MaxPooling2D(pool_size=(5, 5), strides=(2, 2)))

# 2nd convolution layer
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

# 3rd convolution layer
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(AveragePooling2D(pool_size=(3, 3), strides=(2, 2)))

model.add(Flatten())

# fully connected neural networks
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(num_classes, activation='softmax'))
# ------------------------------
# batch process

print(x_train.shape)

gen = ImageDataGenerator()
train_generator = gen.flow(x_train, y_train, batch_size=batch_size)

# ------------------------------

model.compile(loss='categorical_crossentropy'
              , optimizer=keras.optimizers.Adam()
              , metrics=['accuracy']
              )

# ------------------------------

if not os.path.exists("model1.h5"):

    model.fit_generator(train_generator, steps_per_epoch=batch_size, epochs=epochs)
    model.save("model1.h5")  # train for randomly selected one
else:
    model = load_model("model1.h5")  # load weights
from sklearn.metrics import confusion_matrix
yp=model.predict_classes(x_test,verbose=0)
cf=confusion_matrix(y_test,yp)
print(cf)
