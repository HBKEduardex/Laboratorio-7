import cv2

# Iniciar la webcam
cap = cv2.VideoCapture(0)
mode = 'gray'  # Modo inicial

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mostrar según el modo actual
    if mode == 'gray':
        display_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        display_frame = frame  # NO convertir a RGB, dejar como BGR

    cv2.imshow("Webcam", display_frame)

    # Esperar tecla
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Salir
        break
    elif key == ord('g'):  # Modo gris
        mode = 'gray'
    elif key == ord('r'):  # Modo RGB (en realidad BGR para OpenCV)
        mode = 'rgb'

cap.release()
cv2.destroyAllWindows()
