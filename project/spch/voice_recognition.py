import speech_recognition as sr
from tkinter import messagebox

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        try:
            # Add a timeout to avoid waiting indefinitely
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            
            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")
                
                # List of valid commands
                valid_commands = ["launch camera", "capture", "record", "stop", "cancel"]
                
                # If speech is recognized but not a valid command
                if command not in valid_commands:
                    messagebox.showinfo(
                        title="Invalid Command",
                        message=f"'{command}' is not a recognized command.\n\n"
                               "Valid commands are:\n"
                               "• Launch camera - Start the camera\n"
                               "• Capture - Take a photo\n"
                               "• Record - Start recording video\n"
                               "• Stop recording- Stop recording\n"
                               "• Cancel - Exit application"
                    )
                return command
                
            except sr.UnknownValueError:
                # Only show message if audio was detected but not understood
                if recognizer.energy_threshold < audio.energy:
                    messagebox.showwarning(
                        title="Speech Not Recognized",
                        message="Could not understand the audio.\n\n"
                               "Tips for better recognition:\n"
                               "• Speak clearly and at a normal pace\n"
                               "• Reduce background noise\n"
                               "• Keep microphone at proper distance\n"
                               "• Use simple, direct commands"
                    )
                return None
                
        except sr.WaitTimeoutError:
            # No speech detected within timeout period
            print("No speech detected")
            return None
            
        except sr.RequestError:
            # Only show error for network issues when speech was attempted
            messagebox.showerror(
                title="Connection Error",
                message="Could not process speech due to network error.\n\n"
                       "Please check:\n"
                       "• Your internet connection\n"
                       "• Firewall settings\n"
                       "• Network permissions"
            )
            return None
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None
