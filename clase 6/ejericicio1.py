import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Cargar dataset MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalizar datos (0-1 en lugar de 0-255)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Expandir dimensión -> (28, 28, 1) en lugar de (28, 28)
# porque las CNN esperan un canal (grayscale = 1, RGB = 3)
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# 2. Definir el modelo CNN
model = models.Sequential([
    # Primera capa convolucional
    layers.Conv2D(32, (3, 3), activation="relu", input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    # Segunda capa convolucional
    layers.Conv2D(64, (3, 3), activation="relu"),
    layers.MaxPooling2D((2, 2)),
    # Tercera capa convolucional
    layers.Conv2D(64, (3, 3), activation="relu"),
    # Aplanar antes de pasar a capas densas
    layers.Flatten(),
    # Capa densa totalmente conectada
    layers.Dense(64, activation="relu"),
    # Capa de salida -> 10 clases
    layers.Dense(10, activation="softmax") 
])
layers.Dense(10, activation="softmax")

# 3. Compilar
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# 4. Entrenar
model.fit(x_train, y_train, epochs=5, batch_size=64, validation_split=0.1)

# 5. Evaluar en test
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Precisión en test: {test_acc:.2f}")