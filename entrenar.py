import tensorflow as tf

import os

for raiz, _, archivos in os.walk("imagenes"):
    for archivo in archivos:
        if not archivo.lower().endswith((".jpg", ".jpeg", ".png")):
            print("Archivo sospechoso:", os.path.join(raiz, archivo))

dataset = tf.keras.utils.image_dataset_from_directory(
    "imagenes",
    image_size=(224, 224),
    batch_size=4,
    labels="inferred",
    label_mode="int",
)
model = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255, input_shape=(224, 224, 3)),
    tf.keras.layers.Conv2D(16, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(dataset, epochs=10)

model.save("modelo_luna.h5")