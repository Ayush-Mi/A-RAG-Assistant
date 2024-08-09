##############################################
### This code was generated using chatgpt ####
### with few modification ####################
##############################################

import tkinter as tk
from tkinter import scrolledtext
from tkinter.font import Font
from assistant import Assistant

assist = Assistant('db_path')

# Function to handle sending messages
def send_message(event=None):
    user_input = entry.get()
    if user_input:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"You: {user_input}\n", "you")
        
        # response = chatbot_response(user_input)
        response = assist.query(user_input)
        chat_area.insert(tk.END, f"Chatbot: {response}\n", "chatbot")
        
        chat_area.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        chat_area.yview(tk.END)

# Function to clear the chat
def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.config(state=tk.DISABLED)

# Function to close the application
def close_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Chatbot For: Abraham Lincoln Administration 1861")

# Define fonts
text_font = Font(family="Arial", size=14)  # Increase font size for chat_area
entry_font = Font(family="Arial", size=12)  # Font size for entry widget
button_font = Font(family="Arial", size=12)  # Font size for buttons

# Create a text area for chat history
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, font=text_font)
chat_area.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define tags for different colors
chat_area.tag_configure("you", foreground="red")
chat_area.tag_configure("chatbot", foreground="green")

# Create an entry widget for user input
entry = tk.Entry(root, font=entry_font)
entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Create a send button
send_button = tk.Button(root, text="Send", command=send_message, font=button_font)
send_button.grid(row=1, column=1, padx=10, pady=5)

# Create a clear button
clear_button = tk.Button(root, text="Clear", command=clear_chat, font=button_font)
clear_button.grid(row=1, column=2, padx=10, pady=5)

# Create a close button
close_button = tk.Button(root, text="Close", command=close_application, font=button_font)
close_button.grid(row=1, column=3, padx=10, pady=5)


# Configure row and column weights to make widgets expand with the window
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)
root.grid_columnconfigure(2, weight=0)
root.grid_columnconfigure(3, weight=0)

# Bind the Enter key to the send function
root.bind('<Return>', send_message)

# Start the GUI event loop
root.mainloop()
