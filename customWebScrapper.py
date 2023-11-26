from pynput.keyboard import Key, Listener

# Initialize the counter for keypresses
keypress_count = 0

# Define the function to be called when a key is pressed
def on_key_press(key):
    global keypress_count
    keypress_count += 1

# Create a listener that monitors key presses

with Listener(on_press=on_key_press) as listener:
    # Start listening for keypresses
    listener.join()
    input("enter here: ")

# After the listener exits (you can manually stop the script),
# the keypress_count will contain the total number of keypresses.
print(f"Total number of keypresses: {keypress_count}")
