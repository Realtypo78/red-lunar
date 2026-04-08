import sys
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

modelo = tf.keras.models.load_model("modelo_binario_luna.h5")

ruta_imagen = sys.argv[1]

img = image.load_img(ruta_imagen, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

prediccion = modelo.predict(img_array)
clases = ['hay_luna', 'no_luna']

indice = np.argmax(prediccion)
print("Predicción:", clases[indice])
print("Probabilidades:", prediccion[0])