import cv2

# Cargar imagen
image = cv2.imread('mi_imagen.jpg')
height, width = image.shape[:2]

print("Opciones de tamaño:")
print("1. Original")
print("2. Pequeño (25%)")
print("3. Mediano (50%)")
print("4. Grande (200%)")

opcion = input("Selecciona una opción (1-4): ")

if opcion == "1":
    resized = image
elif opcion == "2":
    resized = cv2.resize(image, (width//4, height//4))
elif opcion == "3":
    resized = cv2.resize(image, (width//2, height//2))
elif opcion == "4":
    resized = cv2.resize(image, (width*2, height*2))
else:
    print("Opción inválida. Mostrando original.")
    resized = image

cv2.imshow('Imagen Redimensionada', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
