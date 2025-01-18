from tkinter import PhotoImage

def update_image(label, status):
    """
    Update the image based on the status.

    Args:
        label (Label): The Tkinter label to update the image.
        status (str): The current status (e.g., "listening", "searching", "idle").
    """
    image_path = f"assets/{status}.png"
    new_image = PhotoImage(file=image_path)
    label.config(image=new_image)
    label.image = new_image 


def waiting_to_idle(label):
    """
    Update the image to idle after sleep.
    """
    interval = 2000
    label.after(interval, lambda: update_image(label, "idle"))
    