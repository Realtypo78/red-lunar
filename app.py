import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import streamlit as st

st.set_page_config(page_title="Detector de fases lunares", page_icon="🌙")

modelo = tf.keras.models.load_model("modelo_luna.h5")
clases = ['creciente', 'llena', 'menguante']

st.title("Detector de fases de la luna")
st.warning("⚠️ Este sistema solo debe utilizarse con imágenes del cielo. No está diseñado para analizar otros tipos de imágenes.")
st.write("Sube una imagen del cielo nocturno. El sistema intentará identificar la fase lunar. Si no alcanza suficiente confianza, devolverá 'sin_luna'.")

archivo = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

if archivo is not None:
    img = image.load_img(archivo, target_size=(224, 224))
    st.image(archivo, caption="Imagen cargada", use_container_width=True)

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediccion = modelo.predict(img_array)[0]

    indice = np.argmax(prediccion)
    confianza = float(prediccion[indice])

    if confianza < 0.70:
        resultado = "sin_luna"
    else:
        resultado = clases[indice]

    st.subheader("Resultado")
    st.write(resultado)

    st.subheader("Confianza máxima")
    st.write(round(confianza, 4))

    st.subheader("Probabilidades por clase")
    st.write({
        "creciente": float(prediccion[0]),
        "llena": float(prediccion[1]),
        "menguante": float(prediccion[2]),
    })