from PIL import Image

rutas = {
    "llena": r"imagenes\llena\3eb1f70f3f830415f11ab5fce74adc37.jpg",
    "creciente": r"imagenes\creciente\1000_F_38208120_H4fUOO3dl89twWuOKcwFQ8deCyq3ug02.jpg",
    "menguante": r"imagenes\menguante\1000_F_205747847_0LA99zrhQbbeDZt4gKodm3a9aO6OtcIk.jpg",
    "sin_luna": r"imagenes\sin_luna\3P6E6MK6BNLJ5OO56PF34JYA44.jpg"
}

for nombre, ruta in rutas.items():
    print("Abriendo:", nombre, ruta)
    img = Image.open(ruta)
    img.show()
    input("Presiona Enter para seguir con la siguiente...")