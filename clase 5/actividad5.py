import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Cargar dataset MNIST
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalizar datos (0-1 en lugar de 0-255)
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0

# Aplanar imágenes 28x28 -> vector de 784
x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

# 2. Definir el modelo
model = models.Sequential([
    layers.Dense(128, activation="relu", input_shape=(784,)),
    layers.Dense(64, activation="relu"),
    layers.Dense(10, activation="softmax") # 10 clases (dígitos 0-9)
])

# 3. Compilar
model.compile(optimizer="adam",
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

# 4. Entrenar
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)

# 5. Evaluar en test
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Precisión en test: {test_acc:.2f}")