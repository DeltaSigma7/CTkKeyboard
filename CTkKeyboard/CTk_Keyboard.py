import customtkinter as ctk

is_uppercase = False
is_functional = False

# Define the key layouts
normal_keys_qwertz = [
    ['q', 'w', 'e', 'r', 't', 'z', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['▲', 'y', 'x', 'c', 'v', 'b', 'n', 'm', '←'],
]

normal_keys_qwerty = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['▲', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '←'],
]

functional_keys = [
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
    ['@', '#', '&', '_', '-', '(', ')', '=', '%'],
    ['▲', '"', '*', "'", ':', '/', '!', '+', '←'],
]

keys = normal_keys_qwertz  # Default to QWERTZ

def keyboard(master, widget, layout):
    global normal_keys_qwertz, normal_keys_qwerty, keys

    if layout == "qwertz":
        keys = normal_keys_qwertz
    elif layout == "qwerty":
        keys = normal_keys_qwerty

    # Return text as ctk.StringVar()
    # return_txt = ctk.StringVar()

    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    def close_keyboard(event=None):
        keyboard_frame.destroy()
        entry_frame.destroy()

    def update_keys():
        for frame in keyboard_frame.winfo_children():
            for widget in frame.winfo_children():
                widget.destroy()

        for i, row in enumerate(keys):
            frame = ctk.CTkFrame(keyboard_frame)
            if i == 1:
                frame.grid(row=i, column=0, padx=int((screen_width / len(keys[2])) / 2), sticky="nsew")
            else:
                frame.grid(row=i, column=0, sticky="nsew")
            for j, key in enumerate(row):
                if key == ',':
                    display_key = ';' if is_uppercase else ','
                elif key == '.':
                    display_key = ':' if is_uppercase else '.'
                else:
                    display_key = key.upper() if is_uppercase and key not in ['func', ' ', 'ok', '←'] else key.lower()
                key_btn = ctk.CTkButton(frame, text=display_key, font=("Arial", font_size, "bold"), text_color="black", command=lambda k=display_key: on_key_press(k))
                frame.rowconfigure(0, weight=1)
                frame.columnconfigure(j, weight=1)
                keyboard_frame.rowconfigure(i, weight=1)
                key_btn.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")

        # Update special keys row
        special_row_frame = ctk.CTkFrame(keyboard_frame)
        for j, key in enumerate(special_keys_row):
            if key == ',':
                display_key = ';' if is_uppercase else ','
            elif key == '.':
                display_key = ':' if is_uppercase else '.'
            else:
                display_key = key.upper() if is_uppercase and key not in ['func', ' ', 'ok', '←'] else key.lower()
            key_btn = ctk.CTkButton(special_row_frame, text=display_key, font=("Arial", font_size, "bold"), text_color="black", command=lambda k=display_key: on_key_press(k))
            special_row_frame.columnconfigure(j, weight=1)
            key_btn.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")
            if key == " ":
                special_row_frame.columnconfigure(j, weight=8)
        keyboard_frame.rowconfigure(len(keys), weight=1)
        special_row_frame.grid(row=len(keys), column=0, sticky="nsew")

    def on_key_press(key):
        global is_uppercase, is_functional, keys

        if key == "←":
            txt_entry.delete(len(txt_entry.get()) - 1, 'end')  # Delete the last character
        elif key == "▲":
            is_uppercase = not is_uppercase
            update_keys()
        elif key == 'func':
            is_functional = not is_functional
            keys = functional_keys if is_functional else (normal_keys_qwerty if layout == "qwerty" else normal_keys_qwertz)
            update_keys()
        elif key == 'ok':
            widget.delete(0, ctk.END)
            widget.insert('end', txt_entry.get())
            master.focus()
            close_keyboard()
        else:
            txt_entry.insert('end', key)

    # Create keyboard and layout
    keyboard_frame = ctk.CTkToplevel()
    keyboard_frame.attributes("-topmost", True)
    keyboard_frame.overrideredirect(True)
    keyboard_frame.resizable(False, False)
    font_size = keyboard_frame.winfo_height() / 4
    x = 0
    y = screen_height - (screen_height // 3) - 10
    keyboard_frame.geometry('%dx%d+%d+%d' % (screen_width, screen_height / 3, x, y))
    keyboard_frame.columnconfigure(0, weight=1)

    # Last row for extra keys
    special_keys_row = ['func', ',', ' ', '.', 'ok']
    special_row_frame = ctk.CTkFrame(keyboard_frame)
    for j, key in enumerate(special_keys_row):
        key_btn = ctk.CTkButton(special_row_frame, text=key, font=("Arial", font_size, "bold"), text_color="black", command=lambda k=key: on_key_press(k))
        special_row_frame.columnconfigure(j, weight=1)
        key_btn.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")
        if key == " ":
            special_row_frame.columnconfigure(j, weight=8)
    keyboard_frame.rowconfigure(len(keys), weight=1)
    special_row_frame.grid(row=len(keys), column=0, sticky="nsew")

    for i, row in enumerate(keys):
        frame = ctk.CTkFrame(keyboard_frame)
        if i == 1:
            frame.grid(row=i, column=0, padx=int((screen_width / len(keys[2])) / 2), sticky="nsew")
        else:
            frame.grid(row=i, column=0, sticky="nsew")

        for j, key in enumerate(row):
            key_btn = ctk.CTkButton(frame, text=key, font=("Arial", font_size, "bold"), text_color="black", command=lambda k=key: on_key_press(k))
            frame.rowconfigure(0, weight=1)
            frame.columnconfigure(j, weight=1)
            keyboard_frame.rowconfigure(i, weight=1)
            key_btn.grid(row=0, column=j, padx=5, pady=5, sticky="nsew")

    # Create the keys for the keyboard
    update_keys()

    # Top entry frame for better entry
    entry_frame = ctk.CTkToplevel()
    entry_frame.attributes("-topmost", True)
    entry_frame.overrideredirect(True)
    entry_frame.resizable(False, False)
    entry_frame.focus()
    entry_frame.rowconfigure(0, weight=1)
    entry_frame.rowconfigure(2, weight=1)
    entry_frame.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
    font_size = entry_frame.winfo_height() / 4
    window_height2 = screen_height / 3
    window_width2 = screen_width
    x = (screen_width / 2) - (window_width2 / 2)
    y = (screen_height / 2) - (window_height2 / 2) * 1.5
    entry_frame.geometry('%dx%d+%d+%d' % (window_width2, window_height2, x, y))
    txt_entry = ctk.CTkEntry(entry_frame, height=window_height2 / 4, width=window_width2 / 2, font=("Arial", font_size, "bold"), justify="center")
    txt_entry.grid(row=1, column=1, sticky="nsew", columnspan=4)
    txt_entry.insert('end', widget.get())

    keyboard_frame.focus_force()
    txt_entry.focus_set()
