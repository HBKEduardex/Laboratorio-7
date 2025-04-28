import cv2
import os

# Crear carpeta si no existe
os.makedirs("Captures", exist_ok=True)

# Iniciar la cámara
cap = cv2.VideoCapture(0)
capture_count = 1
last_filename = ""

print("Presiona 'c' para capturar imagen, 'q' para salir")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al acceder a la cámara")
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        last_filename = f"Captures/image{capture_count}.jpg"
        cv2.imwrite(last_filename, frame)
        print(f"[✔] Imagen capturada: {last_filename}")
        capture_count += 1

cap.release()
cv2.destroyAllWindows()

# --------------------------
# Procesamiento de la última imagen
# --------------------------

if last_filename:
    img = cv2.imread(last_filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    mid_h, mid_w = h // 2, w // 2

    Q1 = gray[0:mid_h, 0:mid_w]       # Arriba izquierda
    Q2 = gray[0:mid_h, mid_w:w]       # Arriba derecha
    Q3 = gray[mid_h:h, 0:mid_w]       # Abajo izquierda
    Q4 = gray[mid_h:h, mid_w:w]       # Abajo derecha

    # Mostrar cuadrantes
    cv2.imshow("Cuadrante 1", Q1)
    cv2.imshow("Cuadrante 2", Q2)
    cv2.imshow("Cuadrante 3", Q3)
    cv2.imshow("Cuadrante 4", Q4)

    print("Presiona 'q' para cerrar los cuadrantes")

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
else:
    print("No se capturó ninguna imagen.")
