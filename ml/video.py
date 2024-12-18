import cv2
from cv2 import imshow

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Camera not found")
    exit()
else:
    # Define the codec and create videowriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")  # For .AVI XVID

    out = cv2.VideoWriter("captured_video.avi", fourcc, 20.0, (640, 480))
    while True:

        result, frame = camera.read()
        if not result:
            print("Unable to capture the frame")
            break
        out.write(frame)

        imshow("Video Capture", frame)

        key = cv2.waitKey(1)

        if key == ord("q"):
            # cv2.imwrite("captured_frame.jpg", frame)
            print("video saved")
            break
        elif key == ord("c"):
            print("Capture cancelled")
            break
    out.release()

camera.release()
cv2.destroyAllWindows()
