import speech_recognition as sr
from commands import handle_command
from image_handler import update_image

def start_voice_command_listener(label, bring_to_top, bring_to_down):
    """
    Continuously listens for voice commands and triggers the callback 
    when the correct command is recognized.

    Args:
        label (Label): The Tkinter label to update the image.
        bring_to_top (function): A function to bring the window to the top.
        bring_to_down (function): A function to minimize the window.
    """
    recognizer = sr.Recognizer()

    while True:
        with sr.Microphone() as source:
            print("Listening... Please say something.")
            try:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")

                handle_command(command, label, bring_to_top, bring_to_down)
                
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                update_image(label, "idle")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                update_image(label, "idle")
