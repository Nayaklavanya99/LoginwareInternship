# import tkinter as tk
# from tkinter import messagebox
# from loginwareIn.project.spch.voice_recognition import listen_for_command
# from loginwareIn.project.camera.camera_control import (
#     launch_camera,
#     take_picture,
#     start_recording,
#     save_video,
#     close_camera,
#     preview_camera,
# )


# def process_command(command):
#     if command == "launch camera":
#         launch_camera()
#         root.after(100, preview_camera)
#     elif command == "click":
#         take_picture()
#     elif command == "record":
#         start_recording()
#         root.after(100, preview_camera)
#     elif command == "save":
#         save_video()
#     elif command == "cancel":
#         close_camera()
#         quit()
#     else:
#         print("Command not recognized.")


# def check_for_commands():
#     command = listen_for_command()
#     if command:
#         process_command(command)

#     root.after(500, check_for_commands)


# def create_gui():
#     global root
#     root = tk.Tk()
#     root.title("Voice-Controlled Camera App")
#     root.geometry("400x300")

#     label = tk.Label(root, text="Voice-Controlled Camera App", font=("Arial", 16))
#     label.pack(pady=20)

#     start_button = tk.Button(
#         root,
#         text="Start Voice Commands",
#         command=check_for_commands,  # Start checking for commands
#         bg="green",
#         fg="white",
#     )
#     start_button.pack(pady=10)

#     quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="white")
#     quit_button.pack(pady=10)

#     root.mainloop()


# if __name__ == "__main__":
#     create_gui()


import tkinter as tk
from tkinter import messagebox
from loginwareIn.project.spch.voice_recognition import listen_for_command
from loginwareIn.project.camera.camera_control import (
    launch_camera,
    take_picture,
    start_recording,
    save_video,
    close_camera,
    preview_camera,
)
import threading  # Import threading module

# from loginwareIn.project.database.db_handler import log_action


def process_command(command):
    if command == "launch camera":
        launch_camera()
        # Launch preview in a separate thread so it doesn't block further commands
        # preview_thread = threading.Thread(target=preview_camera)
        # preview_thread.start()
        # log_action("Camera launched")
    elif command == "capture":
        take_picture()
        # log_action("Picture taken")
    elif command == "record":
        start_recording()
        # Launch preview in a separate thread for recording
        # preview_thread = threading.Thread(target=preview_camera)
        # preview_thread.start()
        # log_action("Recording started")
    elif command == "done":
        save_video()
        # log_action("Video saved")
    elif command == "cancel":
        close_camera()
        # log_action("Camera closed")
        quit()
    else:
        print("Command not recognized.")


def start_voice_commands():
    while True:
        command = listen_for_command()
        if command:
            process_command(command)


def create_gui():
    root = tk.Tk()
    root.title("Voice-Controlled Camera App")
    root.geometry("400x300")

    label = tk.Label(root, text="Voice-Controlled Camera App", font=("Arial", 16))
    label.pack(pady=20)

    start_button = tk.Button(
        root,
        text="Start Voice Commands",
        command=start_voice_commands,
        bg="green",
        fg="white",
    )
    start_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="white")
    quit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()
