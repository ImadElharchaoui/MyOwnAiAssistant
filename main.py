from tkinter import *
import ctypes
import threading
from voice_command import start_voice_command_listener


SCREEN_WIDTH = 400
# Function to bring the Tkinter window to the top
def bring_to_top():
    root.deiconify()  # Show the window if it is minimized
    root.attributes("-topmost", True)  #
    root.update()

def bring_to_down():
    root.minsize()
    root.attributes("-topmost", False)
    
    root.after(500,root.withdraw)


# Create the Tkinter window
root = Tk()
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_WIDTH}")
root.configure(bg="white")
root.wm_attributes('-transparentcolor', 'white')
root.overrideredirect(True)

# Get screen width and height
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# Calculate position for bottom right corner
x = screen_width - SCREEN_WIDTH
y = screen_height - SCREEN_WIDTH
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_WIDTH}+{x}+{y}")

# Load the initial image
photoimage = PhotoImage(file="assets/idle.png")
width, height = photoimage.width(), photoimage.height()
label = Label(root, bg="white", width=width, height=height, image=photoimage)
label.image = photoimage  # Keep a reference to avoid garbage collection
label.pack()

# Run the voice recognition in a separate thread
threading.Thread(target=start_voice_command_listener, args=(label, bring_to_top, bring_to_down), daemon=True).start()

# Start the Tkinter main loop
root.mainloop()
