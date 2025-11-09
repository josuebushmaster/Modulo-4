import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

#1 generar datos secuenciales
x=[]
y=[]
for i in range(1000):
    x.append([i, i+1, i+2])
    y.append(i+3)

#2 preparar datos
x = np.array(x)
y = np.array(y)

#RNN espera input 3D: (muestra, pasos temporales, características)
x = x.reshape((x.shape[0], x.shape[1], 1))

#3 construir el modelo rnn
model = Sequential([
    SimpleRNN(50, activation='relu', input_shape=(3, 1)),
    Dense(1)
])

#4 compilar el modelo y entrenar
model.compile(optimizer='adam', loss='mse')
model.fit(x, y, epochs=200, verbose=0)

#5. probar predicciones
entrada=np.array([[97, 98, 99]]).reshape((1, 3, 1))
prediccion = model.predict(entrada)
print(f'Predicción para entrada {entrada.flatten().tolist()}: {prediccion.flatten()[0]}')