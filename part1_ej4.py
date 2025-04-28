import cv2

# Cargar imagen
image = cv2.imread('mi_imagen.jpg')
cv2.imshow('Imagen Original', image)
cv2.waitKey(0)

# Redimensionar a 400x600 (ancho x alto)
resized = cv2.resize(image, (400, 600))
cv2.imshow('Redimensionada', resized)
cv2.waitKey(0)

# Cortar horizontalmente
top_half = resized[:300, :]
bottom_half = resized[300:, :]
cv2.imshow('Mitad Superior', top_half)
cv2.imshow('Mitad Inferior', bottom_half)
cv2.waitKey(0)

# Cortar verticalmente
left_half = resized[:, :200]
right_half = resized[:, 200:]
cv2.imshow('Mitad Izquierda', left_half)
cv2.imshow('Mitad Derecha', right_half)
cv2.waitKey(0)

# Dividir en 4 cuadrantes
q1 = resized[:300, :200]
q2 = resized[:300, 200:]
q3 = resized[300:, :200]
q4 = resized[300:, 200:]

cv2.imshow('Cuadrante 1', q1)
cv2.imshow('Cuadrante 2', q2)
cv2.imshow('Cuadrante 3', q3)
cv2.imshow('Cuadrante 4', q4)
cv2.waitKey(0)
cv2.destroyAllWindows()
