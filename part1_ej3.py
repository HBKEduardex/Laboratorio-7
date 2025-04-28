import cv2

# Cargar imagen
image = cv2.imread('mi_imagen.jpg')

while True:
    cv2.imshow('Imagen', image)
    key = cv2.waitKey(0)

    if key == 27:  # ESC para salir
        break

    # Rotar 90 grados en sentido antihorario
    image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.destroyAllWindows()
