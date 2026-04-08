# Detector de fases de la luna

Aplicación desarrollada en Python, TensorFlow y Streamlit para analizar imágenes del cielo nocturno e identificar la fase de la luna.

## Funcionalidad

El sistema intenta clasificar una imagen en una de estas fases:

- cuarto creciente
- luna llena
- cuarto menguante

Si ninguna de las fases alcanza el umbral mínimo de confianza, devuelve:

- sin_luna

## Importante

Esta aplicación fue diseñada **únicamente para imágenes del cielo**.  
No debe utilizarse con fotos de animales, personas, objetos u otras escenas no relacionadas.

## Tecnologías utilizadas

- Python 3.11
- TensorFlow / Keras
- Streamlit
- Pillow
- NumPy

## Ejecución local

```bash
py -3.11 -m streamlit run app.py

## Autor

Santiago Pérez Valle
