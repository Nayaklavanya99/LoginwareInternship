import tkinter as tk
from tkinter import messagebox
from loginwareIn.project.spch.voice_recognition import listen_for_command
from loginwareIn.project.camera.camera_control import (
    launch_camera,
    take_picture,
    start_recording,
    save_video,
    close_camera,

)
import threading  

# commands_frame = None
def toggle_commands():
    if commands_frame.winfo_ismapped():
        commands_frame.pack_forget()  # Hide the commands section
    else:
        commands_frame.pack(pady=20)


def process_command(command):
    if command == "launch camera":
        launch_camera()
    elif command == "capture":
        take_picture()
    elif command == "record":
        start_recording()
    elif command == "stop":
        save_video()
    elif command == "cancel":
        close_camera()
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
    root.geometry("400x500")
    root.config(bg="#f2f2f2")

    # Title Label
    label = tk.Label(
        root,
        text="Voice-Controlled Camera App",
        font=("Arial", 16, "bold"),
        bg="#f2f2f2",
        fg="#333",
    )
    label.pack(pady=20)

    # Start Voice Command Button
    start_button = tk.Button(
        root,
        text="Start Voice Commands",
        command=start_voice_commands,
        bg="#4CAF50",  # Green color
        fg="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=5,
    )
    start_button.pack(pady=10)

    # Quit Button
    quit_button = tk.Button(
        root,
        text="Quit",
        command=root.quit,
        bg="#F44336",  # Red color
        fg="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=5,
    )
    quit_button.pack(pady=10)
    # Frame for displaying the commands (Initially hidden)
    global commands_frame 
    commands_frame = tk.Frame(root, bg="#f2f2f2")
    commands = [
        ("Launch Camera", "Activate the camera for video capture."),
        ("Capture", "Take a snapshot using the camera."),
        ("Record", "Start recording a video."),
        ("Stop", "Stop the ongoing recording."),
        ("Cancel", "Cancel the current action or exit."),
    ]

    # Add commands to the frame
    for command, description in commands:
        command_label = tk.Label(
            commands_frame,
            text=f"{command}: {description}",
            font=("Arial", 10),
            bg="#f2f2f2",
            anchor="w",
        )
        command_label.pack(pady=5, padx=20)

    # Expandable Section for Usable Commands
    expand_button = tk.Button(
        root,
        text="Usable Commands (Click to Expand)",
        command=toggle_commands,
        bg="#2196F3",  # Blue color
        fg="white",
        font=("Arial", 12, "bold"),
        relief="raised",
        bd=5,
    )
    expand_button.pack(pady=10)


    root.mainloop()


if __name__ == "__main__":
    create_gui()
