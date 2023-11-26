import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Disappearing Text Writer")
window.geometry("400x300")

# Function to handle the button click
def disappear_text():
    text = text_entry.get()  # Get the text from the entry widget
    text_label.config(text=text)  # Set the label text
    text_entry.delete(0, tk.END)  # Clear the entry widget
    window.after(3000, clear_label)  # Schedule clearing the label after 3 seconds

# Function to clear the label
def clear_label():
    text_label.config(text="")

# Create the text entry widget
text_entry = tk.Entry(window, font=("Arial", 12))
text_entry.pack(pady=10)

# Create the button
button = tk.Button(window, text="Display Text", command=disappear_text)
button.pack(pady=10)

# Create the label to display the text
text_label = tk.Label(window, text="", font=("Arial", 16))
text_label.pack()

# Run the main event loop
window.mainloop()
