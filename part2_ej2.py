import cv2

def rgb_to_grayscale(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print("No se pudo abrir la imagen.")
        return
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Grayscale", gray_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Ejemplo de uso:
rgb_to_grayscale("colors/red.jpeg")
