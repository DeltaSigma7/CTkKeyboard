# CTkKeyboard
A virtual keyboard for CustomTkinter, making it easy to enter text on a Raspberry Pi with a touch display.

## Features

- **QWERTZ and QWERTY Layouts**: Supports both QWERTZ and QWERTY keyboard layouts for different user preferences.
- **Enhanced Focus**: Ensures improved focus with a dedicated entry for better text input.
- **Touch-Friendly**: Designed specifically for touch displays, perfect for Raspberry Pi projects.
- **Special keys**: Ensure easy entry of numbers and special characters.
- **Open Source**: Free to use and modify.

## Installation
```bash
pip install CTkKeyboard
```


## Example
```python
import customtkinter as ctk
from CTk_Keyboard import keyboard

#Setup Ctk window
app = ctk.CTk()

app.title("CTkKeyboard_example")

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

#configure window size
window_width = screen_width // 2
window_height = screen_height // 2
app.geometry(f"{window_width}x{window_height}+{screen_width//4}+{screen_height//4}")

#Create entry to bind keyboard
entry = ctk.CTkEntry(app, placeholder_text="Entry",justify="center", font=("Arial", 32, "bold"))
entry.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

#Bind Keyboard on FocusIn event 
entry.bind("<FocusIn>", lambda e: keyboard(app,entry,"qwerty"))

app.mainloop()
```


## Options

| Option  | Description                                      |
|---------|--------------------------------------------------|
| Master  | CustomTkinter main window                        |
| Widget  | Entry widget to bind keyboard                    |
| Layout  | Layout to choose "QWERTZ" or "QWERTY"            |


## Usage

To use CTkKeyboard in your project, follow these steps:

- **Bind the Keyboard**: Bind the keyboard to the entry widget, and it should appear automatically when the entry widget is focused.
  
- **Run your code**: Execute your code.

- **Focus entry**: Tap into the entry and the Keyboard will appear.

- **Type your text**: Type the word you want to insert. If you need to input special characters, press the "func" button.

- **Confirm entry**: Hit the "ok" button to confirm the entry, and the keyboard should disappear.

## Preview
### Qwerty Upper-Case
![Example_img](https://github.com/CadamTechnology/CTkKeyboard/assets/171271702/7e71262d-d125-4616-becb-fdabf6a4e076)
### Qwerty Lower-case
![Example_img_2](https://github.com/CadamTechnology/CTkKeyboard/assets/171271702/30b4476f-8e2a-4da7-8143-6ea127ba5758)
### Special Keys
![Example_img_3](https://github.com/CadamTechnology/CTkKeyboard/assets/171271702/ce14f902-c368-40dc-a0d1-46f7809c05a8)



## Credits

Note: Parts of the code in this example are from [CustomTkinter][1]

If you find my code helpful and would like to support me, feel free to buy me a Ko-fi. However, if you don't want to, that's okay too!

I'm always open to feedback to improve this project further!

[1]: https://github.com/TomSchimansky/CustomTkinter

