import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() # Allows us to place diffrent "objects" (buttons and stuff) in diff locations

    def create_button(self, button_text, button_location="bottom", function_to_run=None):
        self.my_btn = tk.Button(self)
        self.my_btn["text"] = button_text
        self.my_btn["command"] = function_to_run
        self.my_btn.pack(side=button_location)

    def create_text(self, the_text, text_location="bottom"):
        self.my_text = tk.Label(self)
        self.my_text["text"] = the_text
        self.my_text.pack(side=text_location)

    #def create_input(self, )

def say_hi():
    print("hi!!!!!!!!")

def say_hello():
    print("hello there.")

def LaunchApp():

    # Initialize a blank window
    root = tk.Tk()
    app = Application(master=root)

    # Application title and Icon
    root.iconbitmap("gui/img/app_icon.ico")
    app.master.title("Application Killer")

    # Set the window size & max and min window size to 400x400
    scr_length = 420
    scr_width = 500
    root.geometry(f"{scr_length}x{scr_width}")
    app.master.minsize(scr_length,scr_width)
    app.master.maxsize(scr_length,scr_width)


    """Application layout, buttons, textboxes etc go here
    """
    #app.display_text("Please enter the name of the program/s you would like to kill", "top")
    app.create_text("Type the name of the application/s you would like to kill", "top")
    app.create_button("Say Hi", function_to_run=say_hi)
    app.create_button("Say Hello", function_to_run=say_hello)

    # Keeps window 'alive'; without this the window instantly closes.
    app.mainloop()


    