import cv2

# Cargar imagen
image = cv2.imread('mi_imagen.jpg')

# Redimensionar a 1000x1000
resized_image = cv2.resize(image, (1000, 1000))

# Mostrar imagen
cv2.imshow('Imagen Redimensionada', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar si querés
# cv2.imwrite('imagen_1000x1000.jpg', resized_image)
