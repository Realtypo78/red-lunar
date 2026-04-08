import tensorflow as tf

dataset = tf.keras.utils.image_dataset_from_directory(
    "imagenes",
    image_size=(128, 128),
    batch_size=4
)

print("Clases:", dataset.class_names)

for imagenes, etiquetas in dataset.take(1):
    print("Shape imágenes:", imagenes.shape)
    print("Etiquetas:", etiquetas.numpy())