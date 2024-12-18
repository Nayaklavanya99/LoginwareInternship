import cv2
import time

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)
# Use DroidCam's IP stream
# ip_address = "http://192.168.140.132:4747/video"
# cap = cv2.VideoCapture(ip_address)

# Set video properties (forcing correct format)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

if not cap.isOpened():
    print("Error: Cannot access the camera")
    exit()
i = 1
while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture video")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
    )
    j = 1
    for j, (x, y, w, h) in enumerate(faces, 1):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(
            frame,
            str(time.ctime()),
            (20, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_TRIPLEX,
            0.5,
            (211, 211, 211),
            1,
        )

        faceread = f"Person {j}"
        cv2.addText = None
        cv2.putText(
            frame,
            faceread,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 255),
            2,
        )
        # face = cv2.putText(frame,text="Faces Detected",org=(x+50, y-10),fontFace=cv2.FONT_HERSHEY_TRIPLEX,fontScale=0.5,color=(255,0,0),thickness=1)
        # if face detected then show name inn title bar
        # Display window with appropriate title based on face detection

        if len(faces) > 0:
            cv2.imshow("Face detected", frame)
        else:
            cv2.imshow("Face Not detected", frame)
        # cv2.putText(frame, 'Bonki', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
    # cv2.imshow('Face detected', frame)
    # place time stamp at the bottom of frame
    key = cv2.waitKey(1) & 0xFF

    # Save the frame with detected faces when 's' is pressed

    if key == ord("s"):
        if len(faces) > 0:

            cv2.imwrite(f"images/color{i}.jpg", frame)
            i += 1
            cv2.imshow(f"images/color{i}.jpg", frame)

            print("Photo captured and saved as 'captured_face.jpg'")

        else:
            print("No faces detected. Photo not saved.")

    # Exit the loop when 'q' is pressed
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
