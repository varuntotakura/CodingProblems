# Python Stock Prediction Project
# In the Python file, you will be creating a neural network to predict the price of a stock. Part of the program is already implemented, your goal is to set up the model, train the model on the training data set, then finally predict the values from the testing data set.

# These are the following details you need to implement:

# You should create a Sequential model with 5 layers.

# Your model should use 2 LSTM layers, and after each use a Dropout layer with a rate of 0.2. The first LSTM layer should have input_shape as a parameter along with units set to 4. The final layer should be a Dense layer with units set to 1.

# Once the model is set up, you should compile it with a mean_squared_error loss and the optimizer set to adam.

# When you fit the training dataset, make sure to set the following values: epochs=5, batch_size=16, verbose=0

# Finally, print the model summary and then run the predict function on the x_test dataset and print the last column of the array.

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dense, Dropout
import warnings
warnings.filterwarnings('ignore')

def create_dataset(df):
  x = []
  y = []
  for i in range(50, df.shape[0]):
      x.append(df[i-50:i, 0])
      y.append(df[i, 0])
  x = np.array(x)
  y = np.array(y)
  return x, y

# Load and preprocess the dataset
df = pd.read_csv('TSLA.csv')
df = df['Open'].values
df = df.reshape(-1, 1)

# Setup datasets
dataset_train = np.array(df[:int(df.shape[0]*0.8)])
dataset_test = np.array(df[int(df.shape[0]*0.8):])

# Scale the values
scaler = MinMaxScaler(feature_range=(0,1))
dataset_train = scaler.fit_transform(dataset_train)
dataset_test = scaler.transform(dataset_test)

# Use the 'create_dataset' function here on the datasets to create train/test datasets
x_train, y_train = create_dataset(dataset_train)
x_test, y_test = create_dataset(dataset_test)

# Reshape the 'x_train' and 'x_test' datasets
varOcg_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1)  # __define-ocg__
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1)

# Implement the 'Sequential' model here
model = Sequential()

# First LSTM layer with Dropout
model.add(LSTM(units=4, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))

# Second LSTM layer with Dropout
model.add(LSTM(units=4))
model.add(Dropout(0.2))

# Final Dense layer
model.add(Dense(units=1))

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(varOcg_train, y_train, epochs=5, batch_size=16, verbose=0)

# Predict the values for 'x_test'
predictions = model.predict(x_test)

# Print the last column of the 'predictions' array and the model summary
print(predictions[-1])
model.summary()
