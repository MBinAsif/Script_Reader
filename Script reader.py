import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import platform
import pyttsx3

def select_voice(accent):
    voices = {
        1: 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_Zira_11.0',
        2: 'com.apple.speech.synthesis.voice.Karen',  # Australian English
        3: 'com.apple.speech.synthesis.voice.Daniel',  # British English
        4: 'com.apple.speech.synthesis.voice.Veena',  # Indian English
        5: 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_Zira_11.0',  # American English
        6: 'com.apple.speech.synthesis.voice.Fiona',  # New Zealand English
        7: 'com.apple.speech.synthesis.voice.Moira',  # Irish English
        8: 'com.apple.speech.synthesis.voice.Fiona',  # Scottish English
        9: 'com.apple.speech.synthesis.voice.Gwen',  # Welsh English
        10: 'com.apple.speech.synthesis.voice.Deranged',  # Ghanaian English
    }
    return voices.get(accent, '')

def read_with_accent(text, accent):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        if platform.system() == 'Windows':
            engine.setProperty('voice', select_voice(accent))
        elif platform.system() == 'Darwin':
            engine.setProperty('voice', select_voice(accent))
        else:
            engine.setProperty('voice', 'english+f5')
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error occurred while initializing the engine:", e)

def on_read():
    accent_choice = accent_var.get()
    text = text_entry.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", "Please enter text to read.")
        return
    read_with_accent(text, accent_choice)

def on_exit():
    root.destroy()

root = tk.Tk()
root.title("Script Reader")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

accent_var = tk.IntVar()
accent_var.set(1)

accent_label = ttk.Label(main_frame, text="Select the accent:")
accent_label.grid(row=0, column=0, sticky=tk.W)

accent_combobox = ttk.Combobox(main_frame, textvariable=accent_var, values=[
    "English (General)",
    "Australian English",
    "British English",
    "Indian English",
    "American English",
    "New Zealand English",
    "Irish English",
    "Scottish English",
    "Welsh English",
    "Ghanaian English"
])
accent_combobox.grid(row=0, column=1, sticky=tk.W)

text_label = ttk.Label(main_frame, text="Enter the text:")
text_label.grid(row=1, column=0, sticky=tk.W)

text_entry = tk.Text(main_frame, height=5, width=40)
text_entry.grid(row=1, column=1, sticky=(tk.W, tk.E))

read_button = ttk.Button(main_frame, text="Read", command=on_read)
read_button.grid(row=2, column=0, columnspan=2, pady=10)

exit_button = ttk.Button(main_frame, text="Exit", command=on_exit)
exit_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
