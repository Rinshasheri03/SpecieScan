import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np

# Set the directory paths for training and test data (use raw string literals to avoid unicode errors)
train_path = r"C:\Users\user\Pictures\species"  # Replace with your train directory path
test_path = r'C:\Users\user\Pictures\species'   # Replace with your test directory path

# Preprocessing using ImageDataGenerator
train_datagen = ImageDataGenerator(rescale=1./255)  # Normalize images
test_datagen = ImageDataGenerator(rescale=1./255)

# Load training data from the train directory
train_generator = train_datagen.flow_from_directory(
    train_path,
    target_size=(28, 28),  # Resize the images to 28x28 (common size for image classification)
    batch_size=32,
    class_mode='categorical',  # Categorical because we have multiple classes (5 classes in this case)
    color_mode='grayscale'     # Set to 'rgb' if the images are in color
)

# Load test data from the test directory
test_generator = test_datagen.flow_from_directory(
    test_path,
    target_size=(28, 28),
    batch_size=32,
    class_mode='categorical',
    color_mode='grayscale'
)

# Build the RNN model using a simple RNN layer
model = models.Sequential()

# Reshape layer to convert (28, 28, 1) to (28, 28)
model.add(layers.Reshape((28, 28), input_shape=(28, 28, 1)))

# RNN layer that takes the sequence of pixel rows (28 rows, each with 28 pixels)
model.add(layers.SimpleRNN(128, activation='relu'))
model.add(layers.Dense(64, activation='relu'))  # Dense layer for more non-linearity
model.add(layers.Dense(6, activation='softmax'))  # Output layer for 6 classes (softmax for multi-class)

# Compile the model with Adam optimizer and categorical crossentropy loss
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model using the data generators (this will automatically handle batching)
model.fit(train_generator, epochs=5, validation_data=test_generator)

# Evaluate the model performance on the test data
loss, accuracy = model.evaluate(test_generator)
print(f'Test accuracy: {accuracy*100:.2f}%')

# Predicting on a test image
test_image, test_label = test_generator.next()  # Get a batch of images and labels
pred = model.predict(test_image)  # Predict the classes of the test images
predicted_class = np.argmax(pred, axis=1)[0]  # Get the predicted class for the first image in the batch
print(f"Predicted Class for Test Image: {predicted_class}")
