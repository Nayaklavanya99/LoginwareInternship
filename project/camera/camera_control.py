import cv2
import threading

recording_thread = None
camera_thread = None
stop_event = threading.Event()
camera = None
video_writer = None
recording = False


def show_camera():
    global camera
    while not stop_event.is_set():
        ret, frame = camera.read()
        if not ret:
            print("Unable to capture the frame.")
            break

        cv2.imshow("Camera Feed", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Clean up resources
    close_camera()


def launch_camera():
    global camera, camera_thread, stop_event
    if camera is None:
        camera = cv2.VideoCapture(0)
        if not camera.isOpened():
            print("Error: Camera not found!")
            return
        print("Camera launched.")

        # Reset stop_event and start the thread
        stop_event.clear()
        camera_thread = threading.Thread(target=show_camera, daemon=True)
        camera_thread.start()


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
    global camera, video_writer, recording, recording_thread
    if camera is not None and not recording:
        recording = True
        fourcc = cv2.VideoWriter_fourcc(*"XVID")  # For .AVI XVID
        video_writer = cv2.VideoWriter(
            "/loginwareIn/project/assetsss/recorded_video2.avi", fourcc, 20.0, (640, 480)
        )
        print("Recording started.")

        def record_video():
            global recording
            while recording:
                ret, frame = camera.read()
                if not ret:
                    print("Unable to capture the frame.")
                    break
                video_writer.write(frame)

            video_writer.release()
            print("Recording stopped and video saved.")

        recording_thread = threading.Thread(target=record_video)
        recording_thread.start()
    else:
        print("Camera not ready or already recording.")


def save_video():
    global recording, recording_thread
    if recording:
        recording = False
        if recording_thread is not None:
            recording_thread.join()  # Wait for the recording thread to finish
        print("Recording stopped and video saved.")


# def save_video():
#     global video_writer, recording
#     if recording:
#         # recording = False
#         video_writer.release()
#         print("Recording stopped and video saved as 'recorded_video.avi'.")


def close_camera():
    global camera, camera_thread, stop_event
    if camera is not None:
        stop_event.set()  # Signal the camera thread to stop
        if camera_thread and camera_thread.is_alive():
            camera_thread.join()  # Wait for the camera thread to finish

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
