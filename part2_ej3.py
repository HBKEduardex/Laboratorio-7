import cv2
import matplotlib.pyplot as plt

class ColorModifier:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        # Mostrar original usando OpenCV (porque está en BGR)
        plt.imshow(self.image)
        plt.title("Original en BGR")
        plt.axis('off')
        plt.show()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def to_rgb(self):
        rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        plt.imshow(rgb)
        plt.title("RGB")
        plt.axis('off')
        plt.show()

    def to_hsv(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        plt.imshow(hsv)  # HSV puede verse raro en matplotlib, pero igual lo mostramos
        plt.title("HSV")
        plt.axis('off')
        plt.show()

    def to_grayscale(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        plt.imshow(gray, cmap='gray')
        plt.title("Grayscale")
        plt.axis('off')
        plt.show()

# Ejemplo de uso:
modifier = ColorModifier("colors/red.jpeg")
modifier.to_rgb()
modifier.to_hsv()
modifier.to_grayscale()
