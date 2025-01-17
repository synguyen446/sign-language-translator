from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import utils

df = pd.read_csv(r"C:\Users\syngu\GitHub\sign-language-translator\data\sign-language\sign-mnist.csv") # Your training data directory
df_test = pd.read_csv(r"C:\Users\syngu\GitHub\sign-language-translator\data\sign-language\test\test_sample.csv") # Your testing data directory
X_train = df.drop(columns="label")
y_train = df['label']
X_test = df_test.drop(columns= "label")
y_test= df_test["label"]

scaler = StandardScaler()
imgs_train = []
imgs_test = []


X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

y_train = to_categorical(y_train,25)
y_test = to_categorical(y_test,25)


for i in range(len(X_train)):
    pixel_data = X_train[i]
    image = np.array(pixel_data, dtype=np.float32).reshape((28, 28))
    imgs_train.append(image)

for i in range(len(X_test)):
    pixel_data = X_test[i]
    image = np.array(pixel_data, dtype=np.float32).reshape((28, 28))
    imgs_test.append(image)

X_train  = np.array(imgs_train).reshape(-1, 28, 28, 1)
X_test  = np.array(imgs_test).reshape(-1, 28, 28, 1)

model = utils.load_model()
model.fit(X_train,  y_train, epochs= 10, batch_size=128)
model.save("centralized-model.keras")

utils.evaluate(model,X_test,y_test)
utils.visualize(model,X_test,y_test)

