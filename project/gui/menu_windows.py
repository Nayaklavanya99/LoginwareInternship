# menu_windows.py
import tkinter as tk
from tkinter import ttk

class AboutWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("About Us")
        
         # Set window size
        window_width = 600
        window_height = 670

        # Get screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate position for center of screen
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        # Set window size and position
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Make window non-resizable (optional)
        self.window.resizable(False, False)
        
        
        # self.window.geometry("600x650")  # Reduced height
        self.window.config(bg="#f2f2f2")
        
        # Create main frame with scrollbar
        main_frame = tk.Frame(self.window, bg="#f2f2f2")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create canvas and scrollbar
        canvas = tk.Canvas(main_frame, bg="#f2f2f2", highlightthickness=0)  # Removed canvas border
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f2f2f2")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Title
        title = tk.Label(
            scrollable_frame,
            text="About Voice-Controlled Camera App",
            font=("Arial", 16, "bold"),
            bg="#f2f2f2",
            fg="#333"
        )
        title.pack(pady=(0, 20))
        
        # App Description
        self._create_section(scrollable_frame, "Description",
            "This innovative application combines voice recognition technology with camera "
            "control, allowing users to operate their camera hands-free through voice "
            "commands. Perfect for photographers, content creators, and anyone who needs "
            "hands-free camera operation.")
        
        # Features Section
        features_text = (
            "• Voice-controlled camera operations\n"
            "• Hands-free photo capture\n"
            "• Video recording with voice commands\n"
            "• User-friendly interface\n"
            "• Real-time voice command recognition\n"
            "• Multiple camera control options\n"
            "• Instant response system"
        )
        self._create_section(scrollable_frame, "Key Features", features_text)
        
        # Instructions Section
        instructions_text = (
            "1. Launch the Application:\n"
            "   • Start the program\n"
            "   • Click 'Start Voice Commands' button\n\n"
            "2. Voice Commands:\n"
            "   • 'Launch camera' - Opens the camera\n"
            "   • 'Capture' - Takes a photo\n"
            "   • 'Record' - Starts video recording\n"
            "   • 'Stop' - Stops recording\n"
            "   • 'Cancel' - Closes camera/exits\n\n"
            "3. Best Practices:\n"
            "   • Speak clearly and at a normal pace\n"
            "   • Use commands in a quiet environment\n"
            "   • Wait for command confirmation\n"
            "   • Keep a reasonable distance from microphone"
        )
        self._create_section(scrollable_frame, "How to Use", instructions_text)
        
        # Technical Info Section
        tech_info_text = (
            "• Version: 1.0\n"
            "• Python Version: 3.x\n"
            "• Key Libraries: OpenCV, Speech Recognition\n"
            "• Platform: Windows/Linux/MacOS\n"
            "• Last Updated: 2024"
        )
        self._create_section(scrollable_frame, "Technical Information", tech_info_text)
        
        # Credits
        credits_text = (
            "Developed by: Sahil Belurkar & Lavanaya Nayak\n"
            "© 2024 All rights reserved\n"
            "Version 1.0"
        )
        self._create_section(scrollable_frame, "Credits", credits_text)
        
        # Pack scrollbar and canvas
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Bottom frame for close button (separate from scrollable content)
        bottom_frame = tk.Frame(self.window, bg="#f2f2f2")
        bottom_frame.pack(fill=tk.X, pady=(0, 10))  # Reduced bottom padding

        # Close button with hover effect
        def on_enter(e):
            e.widget['background'] = '#c0392b'

        def on_leave(e):
            e.widget['background'] = '#e74c3c'

        # Close button
        close_button = tk.Button(
            bottom_frame,
            text="Close",
            command=self.window.destroy,
            bg="#e74c3c",
            fg="white",
            font=("Arial", 11, "bold"),
            width=15,
            height=1,
            relief="flat",
            cursor="hand2"
        )
        close_button.pack(pady=5)
        close_button.bind("<Enter>", on_enter)
        close_button.bind("<Leave>", on_leave)

    def _create_section(self, parent, title, content):
        """Helper method to create consistent sections"""
        # Section Frame
        section_frame = tk.Frame(parent, bg="#f2f2f2")
        section_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Section Title
        section_title = tk.Label(
            section_frame,
            text=title,
            font=("Arial", 12, "bold"),
            bg="#f2f2f2",
            fg="#2196F3"
        )
        section_title.pack(anchor="w")
        
        # Section Content
        section_content = tk.Label(
            section_frame,
            text=content,
            font=("Arial", 10),
            bg="#f2f2f2",
            justify=tk.LEFT,
            wraplength=500
        )
        section_content.pack(anchor="w", padx=(10, 0))


    def _create_section(self, parent, title, content):
        """Helper method to create consistent sections"""
        # Section Frame
        section_frame = tk.Frame(parent, bg="#f2f2f2")
        section_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Section Title
        section_title = tk.Label(
            section_frame,
            text=title,
            font=("Arial", 12, "bold"),
            bg="#f2f2f2",
            fg="#2196F3"
        )
        section_title.pack(anchor="w")
        
        # Section Content
        section_content = tk.Label(
            section_frame,
            text=content,
            font=("Arial", 10),
            bg="#f2f2f2",
            justify=tk.LEFT,
            wraplength=500
        )
        section_content.pack(anchor="w", padx=(10, 0))


class HomeWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Home")
        self.window.geometry("400x300")
        self.window.config(bg="#f2f2f2")
        
        # Home content
        title = tk.Label(
            self.window,
            text="Welcome to Voice-Controlled Camera App",
            font=("Arial", 14, "bold"),
            bg="#f2f2f2"
        )
        title.pack(pady=20)
        
        features = tk.Label(
            self.window,
            text="Features:\n\n"
                 "• Voice-controlled camera operations\n"
                 "• Take pictures with voice commands\n"
                 "• Record videos using voice\n"
                 "• Simple and intuitive interface",
            font=("Arial", 10),
            bg="#f2f2f2",
            justify="left"
        )
        features.pack(pady=20)
        
        # Close button
        close_button = tk.Button(
            self.window,
            text="Close",
            command=self.window.destroy,
            bg="#F44336",
            fg="white",
            font=("Arial", 10, "bold")
        )
        close_button.pack(pady=10)
