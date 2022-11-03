import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # Используйте 5-ю камеру (5 камер подключены к моему компьютеру)
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml') # Загрузить библиотеку элементов лица

while(True):
    ret, frame = cap.read() # Прочитать кадр изображения
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Поседеть

    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.15, minNeighbors = 5, minSize = (5, 5)) # Обнаружить лицо
    for(x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2) # Обведите лицо прямоугольником

    cv2.imshow('Face Recognition', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Отпустить камеру
cv2.destroyAllWindows()
