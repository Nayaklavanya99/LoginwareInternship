import speech_recognition as sr
from tkinter import messagebox

 
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        
        try:
            # Adjust ambient noise dynamically
            recognizer.adjust_for_ambient_noise(source, duration=1)

            # Add a timeout to avoid waiting indefinitely
            audio = recognizer.listen(source,timeout=5,  phrase_time_limit=3)

            try:
                command = recognizer.recognize_google(audio).lower()
                print(f"Recognized command: {command}")
                
                
                # List of valid commands
                valid_commands = [
                    "launch camera",
                    "capture",
                    "record",
                    "stop recording",
                    "cancel",
                ]

                if command not in valid_commands:
                    messagebox.showinfo(
                        title="Invalid Command",
                        message=f"'{command}' is not a recognized command.\n\n"
                        "Valid commands are:\n"
                        "• Launch camera - Start the camera\n"
                        "• Capture - Take a photo\n"
                        "• Record - Start recording video\n"
                        "• Stop recording - Stop recording\n"
                        "• Cancel - Exit application",
                    )
                                     
                return command

            except sr.UnknownValueError:
                # messagebox.showwarning(
                #     title="Speech Not Recognized",
                #     message="Could not understand the audio.\n\n"
                #     "Tips for better recognition:\n"
                #     "• Speak clearly and at a normal pace\n"
                #     "• Reduce background noise\n"
                #     "• Keep microphone at proper distance\n"
                #     "• Use simple, direct commands",
                # )
                return None

        except sr.WaitTimeoutError:
            print("No speech detected")
            return None

        except sr.RequestError as e:
            messagebox.showerror(
                title="Connection Error",
                message=f"Could not process speech due to network error: {str(e)}",
            )
            return None

        except Exception as e:
            messagebox.showerror(
                title="Error", message=f"An unexpected error occurred: {str(e)}"
            )
            return None
