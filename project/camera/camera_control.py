import cv2

camera = None
video_writer = None
recording = False


def launch_camera():
    global camera
    if camera is None:
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("Error: Camera not found!")
            return
        print("Camera launched.")


def take_picture():
    global camera
    if camera is not None:
        ret, frame = camera.read()
        if ret:
            cv2.imwrite("/loginwareIn/project/assetsss/captured_image.jpg", frame)
            print("Picture taken and saved as 'captured_image.jpg'.")
        else:
            print("Failed to capture image.")
    else:
        print("Camera not launched.")


def start_recording():
    global camera, video_writer, recording
    if camera is not None and not recording:
        recording = True
        fourcc = cv2.VideoWriter_fourcc(*"XVID")  # For .AVI XVID
        video_writer = cv2.VideoWriter(
            "/loginwareIn/project/assetsss/recorded_video.avi", fourcc, 20.0, (640, 480)
        )
        print("Recording started.")

        while recording:
            ret, frame = camera.read()
            if not ret:
                print("Unable to capture the frame.")
                break
            video_writer.write(frame)

        video_writer.release()
        print("Recording stopped and video saved.")


def save_video():
    global recording
    if recording:
        recording = False
        print("Recording stopped and video saved.")


# def save_video():
#     global video_writer, recording
#     if recording:
#         # recording = False
#         video_writer.release()
#         print("Recording stopped and video saved as 'recorded_video.avi'.")


def close_camera():
    global camera
    if camera is not None:
        camera.release()
        cv2.destroyAllWindows()
        camera = None
        print("Camera closed.")


def preview_camera():
    global camera
    if camera is not None:
        while True:
            ret, frame = camera.read()
            if not ret:
                print("Error: Failed to capture frame.")
                break

            # Display the preview in a window
            cv2.imshow("Camera Preview", frame)

            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        close_camera()  
    else:
        print("Camera not launched.")
