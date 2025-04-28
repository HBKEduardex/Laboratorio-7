import cv2
import numpy as np

# Capturar imagen de la cámara
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definiciones para ROJO
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # Definiciones para VERDE
    lower_green = np.array([36, 50, 70])
    upper_green = np.array([89, 255, 255])

    # Definiciones para AZUL
    lower_blue = np.array([90, 50, 70])
    upper_blue = np.array([128, 255, 255])

    # Crear máscaras
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Contar píxeles de cada color
    red_pixels = cv2.countNonZero(mask_red)
    green_pixels = cv2.countNonZero(mask_green)
    blue_pixels = cv2.countNonZero(mask_blue)

    # Definir un umbral de detección
    threshold = 1000

    # Mostrar qué color fue detectado
    if red_pixels > threshold:
        print("🔴 RED detected")
    elif green_pixels > threshold:
        print("🟢 GREEN detected")
    elif blue_pixels > threshold:
        print("🔵 BLUE detected")
    else:
        print("⚪ No color detected")

    # Mostrar la cámara
    cv2.imshow("Camera", frame)

    # Salir si presiono 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
