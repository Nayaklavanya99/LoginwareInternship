import cv2

camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Camera not found")
    exit()
else:
    result,frame = camera.read()
    if not result:
        print("unable to capure the frame")
        exit()
    else:
        cv2.imwrite("test2.jpg",frame)
        print("image saved")
camera.release()