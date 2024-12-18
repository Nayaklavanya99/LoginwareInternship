import cv2
from cv2 import imshow

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Camera not found")
    exit()
else:
    while True:

        # to capture an image
        result, frame = camera.read()
        if not result:
            print("unable to capture the frame")
            break

        # Display the frame
        imshow("press q to capture or c to cancel ", frame)

        # check for keypress
        key = cv2.waitKey(1)

        if key == ord("q"):
            cv2.imwrite("test2.jpg", frame)
            print("image saved")
            break
        elif key == ord("c"):
            print("capture cancelled")
            break

camera.release()
cv2.destroyAllWindows()
