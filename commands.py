import webbrowser
from image_handler import update_image
import os
from subprocess import Popen
import json


EpicGamesLauncher = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
# State variable to track if the bot has been activated
bot_activated = False

def handle_command(command, label, bring_to_top, bring_to_down):
    """
    Handle the recognized voice command.

    Args:
        command (str): The recognized voice command.
        label (Label): The Tkinter label to update the image.
        bring_to_top (function): A function to bring the window to the top.
        bring_to_down (function): A function to minimize the window.
    """
    global bot_activated

    if command.split()[0] == "hello":
        print("Command recognized: Bringing window to top.")
        update_image(label, "listening")
        bring_to_top()
        bot_activated = True
    elif bot_activated:
        if command.split()[0] == "search":
            print("Command recognized: Searching about " + " ".join(command.split()[1:]))
            update_image(label, "searching")
            search_query = command.split()[1:]
            webbrowser.open(f"https://www.google.com/search?q={' '.join(search_query)}")
        elif command.split()[0] == "goodbye":
            print("Command recognized: Minimizing window.")
            update_image(label, "sad")
            bring_to_down()
            bot_activated = False
        elif command.split()[0] == "open":
            update_image(label, "happy")
            with open("Data.json", "r") as file:
                data = json.load(file)
                try:
                    path = str(data[" ".join(command.split()[1:])]["path"])
                    print("path:", path)
                    Popen(path, shell=True)
                except KeyError:
                    print("Cannot open file:", " ".join(command.split()[1:]), "error:", KeyError)
                    update_image(label, "idle")
                
            
        else:
            print("Command not recognized.")
            update_image(label, "idle")
    else:
        print("Please say 'hello' to activate the bot.")
        update_image(label, "idle")
