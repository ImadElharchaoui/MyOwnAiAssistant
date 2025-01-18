import webbrowser
from image_handler import update_image, waiting_to_idle
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

    if command.split()[0] == "johnny":
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
            waiting_to_idle(label)
        elif command.split()[0] == "goodbye":
            print("Command recognized: Minimizing window.")
            update_image(label, "sad")
            bring_to_down()
            bot_activated = False
            waiting_to_idle(label)
        elif command.split()[0] == "open":
            update_image(label, "happy")
            with open("Data.json", "r") as file:
                data = json.load(file)
                try:
                    if len(command.split()) >= 2:
                        entry_type = "games" if "game" == command.split()[1] else "folders"
                        path = ""
                        if(entry_type == "games"):
                            path = str(data[entry_type][" ".join(command.split()[2:])]["path"])
                            Popen(path, shell=True)
                        else:
                            path = str(data[entry_type][" ".join(command.split()[1:])]["path"])
                            os.startfile(path)
                            
                        
                        print("path:", path)
                        
                except KeyError as e:
                    print("Cannot open file:", " ".join(command.split()[1:]), "error:", e)
                    update_image(label, "idle")
            waiting_to_idle(label)
        elif command.split()[0][0:5] == "great":
            update_image(label, "love")
            waiting_to_idle(label)
            pass
        else:
            print("Command not recognized.")
            update_image(label, "idle")
    else:
        print("Please say 'johnny' to activate the bot.")
        update_image(label, "idle")
