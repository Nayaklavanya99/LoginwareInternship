import cv2
import threading
import time 
recording_thread = None
camera_thread = None
stop_event = threading.Event()
camera = None
video_writer = None
recording = False


def show_camera():
    global camera, recording
    current_window = "Camera Feed"  # Initial window name

    while not stop_event.is_set():
        ret, frame = camera.read()
        if not ret:
            print("Unable to capture the frame.")
            break
        # Determine the new window title based on recording status
        new_window = "Recording Feed" if recording else "Camera Feed"
        # timestamp = time.ctime()
        # height, width = frame.shape[:2]

        # # Place the text at the bottom of the frame
        # cv2.putText(
        #     frame,
        #     timestamp,
        #     (10, height - 10),  # Adjust the y-coordinate to place the text at the bottom
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     0.5,  # Smaller font size
        #     (255, 255, 255),  # White color
        #     1,  # Thinner line thickness
        #     cv2.LINE_AA
        # )
        
        # If the window title changes, destroy the current window and create a new one
        if new_window != current_window:
            cv2.destroyWindow(current_window)
            current_window = new_window

        # Display the frame in the updated window
        cv2.imshow(current_window, frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Clean up resources
    close_camera()


def launch_camera():
    global camera, camera_thread, stop_event
    if camera is None:
        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
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
            cv2.imwrite("/loginwareIn/project/assetsss/captured_image1.jpg", frame)
            print("Picture taken and saved as 'captured_image1.jpg'.")
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
            "/loginwareIn/project/assetsss/recorded_video3.avi", fourcc, 20.0,(640,480)
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

closecount=0
def close_camera():
    try:
        global camera, camera_thread, stop_event
        if camera is not None:
            stop_event.set()  # Signal the camera thread to stop
            if camera_thread and camera_thread.is_alive():
                # Check if the current thread is the same as camera_thread
                if camera_thread != threading.current_thread():
                    camera_thread.join()  # Wait for the camera thread to finish
            # print(camera)
            if camera is not None:
                camera.release()
            cv2.destroyAllWindows()
            camera = None
            print("Camera closed.")
    except Exception as e:
        print(f"Closed camera with esception {e}")
