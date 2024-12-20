import tkinter as tk
from tkinter import messagebox
import threading
from loginwareIn.project.gui.menu_windows import AboutWindow
from loginwareIn.project.spch.voice_recognition import listen_for_command
from loginwareIn.project.camera.camera_control import (
    launch_camera,
    take_picture,
    start_recording,
    save_video,
    close_camera,
)

def start_voice_commands():
    """Run voice command listening in a separate thread to avoid blocking the GUI"""
    while True:
        command = listen_for_command()
        if command:
            process_command(command)

def process_command(command):
    if command == "launch camera":
        launch_camera()
    elif command == "capture":
        take_picture()
    elif command == "record":
        start_recording()
    elif command == "stop recording":
        save_video()
    elif command == "cancel":
        close_camera()
        quit()
    else:
        print("Command not recognized.")
def start_voice_thread():
    """Start voice command thread to keep GUI responsive"""
    voice_thread = threading.Thread(target=start_voice_commands, daemon=True)
    voice_thread.start()
class VoiceCommandThread(threading.Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def run(self):
        while not self._stop_event.is_set():
            command = listen_for_command()
            if command is None:
                continue  # Skip if no command was understood
                
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
                self.stop()
                break

def create_gui():
    root = tk.Tk()
    root.title("Voice-Controlled Camera App")
    root.geometry("1920x1080")
    root.config(bg="#f5f6fa")

    # Create menubar
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    voice_thread = None

    # def start_voice_command_thread():
    #     nonlocal voice_thread
    #     if voice_thread is None or not voice_thread.is_alive():
    #         voice_thread = VoiceCommandThread()
    #         voice_thread.start()
    #         start_button.config(state='disabled')
    #         quit_button.config(state='normal')

    def stop_voice_commands():
        nonlocal voice_thread
        if voice_thread and voice_thread.is_alive():
            voice_thread.stop()
            voice_thread.join()  # Ensure the thread has finished executing
            voice_thread = None
        root.quit()  # Terminate the mainloop
        root.destroy()

    def open_home():
        root.lift()
        root.focus_force()

    def open_about():
        about_window = AboutWindow()

    def on_closing():
        if voice_thread and voice_thread.is_alive():
            voice_thread.stop()
        root.quit()
        root.destroy()

    # Add menu items
    menubar.add_command(label="Home", command=open_home)
    menubar.add_command(label="About Us", command=open_about)

    # Main container
    main_container = tk.Frame(root, bg="#f5f6fa")
    main_container.pack(expand=True, fill="both", padx=50, pady=30)

    # Title Frame
    title_frame = tk.Frame(main_container, bg="#f5f6fa")
    title_frame.pack(fill="x", pady=(0, 20))

    label = tk.Label(
        title_frame,
        text="Voice-Controlled Camera App",
        font=("Helvetica", 28, "bold"),
        bg="#f5f6fa",
        fg="#2c3e50",
    )
    label.pack(pady=(10, 5))

    subtitle = tk.Label(
        title_frame,
        text="Control your camera with simple voice commands",
        font=("Helvetica", 14),
        bg="#f5f6fa",
        fg="#7f8c8d",
    )
    subtitle.pack(pady=(0, 10))

    # Center content frame
    center_frame = tk.Frame(main_container, bg="#f5f6fa")
    center_frame.pack(expand=True, fill="both")

    # Main control box with gradient-like effect
    control_box_outer = tk.Frame(
        center_frame,
        bg="#3498db",
        relief="flat",
        bd=0,
    )
    control_box_outer.pack(pady=20, padx=300)

    # Create gradient effect with multiple frames
    gradient_colors = ["#3498db", "#2980b9", "#2574a9"]
    gradient_frames = []
    for color in gradient_colors:
        frame = tk.Frame(control_box_outer, bg=color, bd=0, height=2)
        frame.pack(fill="x")
        gradient_frames.append(frame)

    # Main content box
    control_box = tk.Frame(
        control_box_outer,
        bg="#f8f9fa",
        relief="flat",
        bd=0,
    )
    control_box.pack(fill="both", padx=2, pady=2)

    # Inner frame for padding
    inner_frame = tk.Frame(control_box, bg="#f8f9fa", padx=40, pady=30)
    inner_frame.pack(fill="both")

    # Info icon and commands display
    info_frame = tk.Frame(inner_frame, bg="#f8f9fa")
    info_frame.pack(fill="x", pady=(0, 20))

    # Create a custom info icon
    info_label = tk.Label(
        info_frame,
        text="ⓘ",
        font=("Helvetica", 18),
        bg="#f8f9fa",
        fg="#3498db",
        cursor="hand2"
    )
    info_label.pack(side="right", padx=5)

    # Commands popup
    commands_popup = tk.Toplevel(root)
    commands_popup.withdraw()
    commands_popup.overrideredirect(True)
    commands_popup.configure(bg="#2c3e50")

    # Add inner frame for popup content
    popup_inner = tk.Frame(commands_popup, bg="white", padx=10, pady=10)
    popup_inner.pack(padx=2, pady=2)

    # Add commands to popup
    commands = [
        ("Launch Camera", "Activate the camera"),
        ("Capture", "Take a photo"),
        ("Record", "Start recording"),
        ("Stop recording", "Stop recording"),
        ("Cancel", "Exit camera")
    ]

    for cmd, desc in commands:
        cmd_frame = tk.Frame(popup_inner, bg="white")
        cmd_frame.pack(fill="x", pady=3)
        
        tk.Label(
            cmd_frame,
            text=cmd,
            font=("Helvetica", 10, "bold"),
            bg="white",
            fg="#3498db"
        ).pack(side="left")
        
        tk.Label(
            cmd_frame,
            text=f": {desc}",
            font=("Helvetica", 10),
            bg="white",
            fg="#7f8c8d"
        ).pack(side="left", padx=(5, 0))

    def show_commands(event):
        x = info_label.winfo_rootx()
        y = info_label.winfo_rooty()
        commands_popup.geometry(f"+{x-200}+{y-commands_popup.winfo_reqheight()-10}")
        commands_popup.deiconify()

    def hide_commands(event):
        commands_popup.withdraw()

    info_label.bind("<Enter>", show_commands)
    info_label.bind("<Leave>", hide_commands)
    commands_popup.bind("<Leave>", hide_commands)

    # Start Voice Command Button
    def on_enter(e):
        e.widget.configure(bg='#2ecc71')

    def on_leave(e):
        e.widget.configure(bg='#27ae60')

    start_button = tk.Button(
        inner_frame,
        text="Start Voice Commands",
        command=start_voice_thread,
        bg="#27ae60",
        fg="white",
        font=("Helvetica", 16, "bold"),
        relief="flat",
        bd=0,
        padx=40,
        pady=20,
        cursor="hand2"
    )
    start_button.pack(pady=(0, 20))
    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)

    # Separator
    separator = tk.Frame(inner_frame, height=1, bg="#e0e6ed")
    separator.pack(fill="x", pady=20)

    # Quit Button
    def on_enter_quit(e):
        e.widget.configure(bg='#c0392b')

    def on_leave_quit(e):
        e.widget.configure(bg='#e74c3c')

    quit_button = tk.Button(
        inner_frame,
        text="Quit Application",
        command=stop_voice_commands,
        bg="#e74c3c",
        fg="white",
        font=("Helvetica", 16, "bold"),
        relief="flat",
        bd=0,
        padx=40,
        pady=20,
        cursor="hand2"
        # Removed the state='disabled' to make the quit button always active
    )
    quit_button.pack()
    quit_button.bind("<Enter>", on_enter_quit)
    quit_button.bind("<Leave>", on_leave_quit)

    # Bind window closing event
    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
