import cv2
import os

# Asegurarse que existe la carpeta
folder = "colors"
colors = ["red.jpeg", "green.jpg", "blue.jpeg"]

for color_img in colors:
    path = os.path.join(folder, color_img)
    image = cv2.imread(path)

    if image is not None:
        # Obtiene el color promedio
        average_color = image.mean(axis=0).mean(axis=0)
        print(f"Color promedio de {color_img}: {average_color}")
    else:
        print(f"No se pudo abrir {path}")
