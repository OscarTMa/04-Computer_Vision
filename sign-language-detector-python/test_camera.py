import cv2

# Cambia el índice de la cámara según sea necesario
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Captura frame-by-frame
    ret, frame = cap.read()
    
    # Si el frame se lee correctamente, ret es True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Muestra el frame resultante
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

# Cuando todo está hecho, libera la captura
cap.release()
cv2.destroyAllWindows()
