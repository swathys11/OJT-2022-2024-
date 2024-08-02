import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam # type: ignore
import numpy as np


def weighted_binary_crossentropy(weights):
    def loss(y_true, y_pred):
        # Calculate the binary cross-entropy
        bce = K.binary_crossentropy(y_true, y_pred)
        
        # Apply the weights to the loss
        weight_vector = y_true * weights[1] + (1. - y_true) * weights[0]
        weighted_bce = weight_vector * bce
        
        return K.mean(weighted_bce)
    return loss

# Define a simple binary classification model
model = Sequential([
    Dense(32, input_shape=(10,), activation='relu'),
    Dense(1, activation='sigmoid')
])

# Define weights for the custom loss function (e.g., class 0: 0.5, class 1: 2.0)
weights = [0.5, 2.0]

# Compile the model using the custom loss function
model.compile(optimizer=Adam(), loss=weighted_binary_crossentropy(weights), metrics=['accuracy'])

# Generate some dummy data
np.random.seed(42)
x_train = np.random.rand(1000, 10)
y_train = np.random.randint(2, size=1000)

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, verbose=1)

# Generate dummy test data
x_test = np.random.rand(200, 10)
y_test = np.random.randint(2, size=200)

# Evaluate the model
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])