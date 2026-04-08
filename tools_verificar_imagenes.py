from PIL import Image
import os

carpeta_base = "imagenes"

for raiz, _, archivos in os.walk(carpeta_base):
    for archivo in archivos:
        ruta = os.path.join(raiz, archivo)
        try:
            with Image.open(ruta) as img:
                img.verify()
            print("OK:", ruta)
        except Exception as e:
            print("ERROR:", ruta, "->", e)