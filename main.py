import cv2
import winsound
winsound.Beep(1000, 500)

# Load face detection model
face_cascade = cv2.CascadeClassifier(
    "models/haarcascade_frontalface_default.xml"
)

# Open webcam
cap = cv2.VideoCapture(0)

print("Camera started... Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    # Draw rectangles
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

    cv2.imshow("Screen Privacy Guard", frame)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
if len(faces) > 1:
    cv2.putText(
        frame,
        "PRIVACY ALERT: Someone is watching!",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )
