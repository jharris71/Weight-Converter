# Import Module
from tkinter import Tk, Label, Entry, Button, Frame

def get_entry_value():
    try:
        value = float(weight_Entry.get())
        if value < 0:
             Result_lbl.config(text = "Weight cannot be negative")
             return None
        return value
    except ValueError:
        Result_lbl.config(text = "Please Enter a Number first")
        return None

def calculate_grams(weight):
     return weight * 1000 

def calculate_ounces(weight):
     return weight * 35.274

def calculate_pounds(weight):
     return weight * 2.20462

def convert_to_grams():
    weight_grams = get_entry_value()
    if weight_grams is None:
        return
    conversion_grams = calculate_grams(weight_grams)
    Result_lbl.config(text = f"{conversion_grams:.2f}")
    return conversion_grams

def convert_to_ounces():
    weight_ounces = get_entry_value()
    if weight_ounces is None:
            return
    conversion_ounces = calculate_ounces(weight_ounces)
    Result_lbl.config(text = f"{conversion_ounces:.2f}")
    return conversion_ounces

def convert_to_pounds():
    weight_pounds = get_entry_value()
    if weight_pounds is None:
            return
    conversion_pounds = calculate_pounds(weight_pounds)
    Result_lbl.config(text = f"{conversion_pounds:.2f}")
    return conversion_pounds

def on_hover(event):
     event.widget.config(bg = "#2563EB")

def on_leave(event):
     event.widget.config(bg = "#3B82F6")


def create_window():
    global weight_Entry, Result_lbl
     

    # Create a root window
    root = Tk()

    # Root Window and Title
    root.title("Weight Converter")

    # set geometry (widthxheight)
    root.geometry("500x400")

    # Create a Label
    Title_lbl = Label(root,
        text = "Weight Converter",
        font = ("arial",20)
        )

    Title_lbl.pack(pady=30)

    # Create sub label
    Instruction_lbl = Label(root,
            text = "Enter the Weight in kilograms:",
            font = ("Arial",14)
            )

    Instruction_lbl.pack(pady=10)

    #Creating input Entry
    weight_Entry = Entry(root, 
                        text = "" ,
                        font = ("Arial",12)
                        )

    weight_Entry.pack(pady=10)

    # Create a frame to hold the buttons
    button_frame = Frame(root)
    button_frame.pack(pady=10)

    Button_grams = Button(button_frame,
                        text = "grams",
                        font = ("Arial",11, "bold"),
                        bg = "#3B82F6",
                        fg = "white",
                        activebackground = "#2563EB",
                        activeforeground = "white",
                        command = convert_to_grams
                        )

    Button_grams.pack(side = "left",  padx = 10)
    Button_grams.bind("<Enter>", on_hover)
    Button_grams.bind("<Leave>", on_leave)

    Button_ounces = Button(button_frame,
                        text = "ounces",
                        font = ("Arial",11, "bold"),
                        bg = "#3B82F6",
                        fg = "white",
                        activebackground = "#2563EB",
                        activeforeground = "white",
                        command = convert_to_ounces
                        )

    Button_ounces.pack(side = "left", padx = 10)
    Button_ounces.bind("<Enter>", on_hover)
    Button_ounces.bind("<Leave>", on_leave)

    Button_pounds = Button(button_frame,
                        text = "pounds",
                        font = ("Arial",11, "bold"),
                        bg = "#3B82F6",
                        fg = "white",
                        activebackground = "#2563EB",
                        activeforeground = "white",
                        command = convert_to_pounds
                        )

    Button_pounds.pack(side = "left", padx = 10)
    Button_pounds.bind("<Enter>", on_hover)
    Button_pounds.bind("<Leave>", on_leave)

    Result_lbl = Label(root,
            text = "Result will appear here",
            font = ("Arial",16, "bold"),
            )

    Result_lbl.pack(pady=12)
    return root


# Set running event loop 
if __name__ == "__main__":
     root = create_window()
     root.mainloop()
