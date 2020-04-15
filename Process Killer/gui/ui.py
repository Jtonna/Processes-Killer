import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack() # Allows us to place diffrent "objects" (buttons and stuff) in diff locations

    def create_button(self, button_text, button_location="bottom"):
        self.my_btn = tk.Button(self)
        self.my_btn["text"] = button_text
        self.my_btn.pack(side=button_location)

    def create_text(self, the_text, text_location="bottom"):
        self.my_text = tk.Label(self)
        self.my_text["text"] = the_text
        self.my_text.pack(side=text_location)



def LaunchApp():

    # Initialize a blank window
    root = tk.Tk()
    app = Application(master=root)

    # Application title and Icon
    root.iconbitmap("gui/img/app_icon.ico")
    app.master.title("Application Killer")

    # Set the max and min window size to 400x400
    app.master.minsize(400,400)
    app.master.maxsize(400,400)

    """Application layout, buttons, textboxes etc go here
    """
    #app.display_text("Please enter the name of the program/s you would like to kill", "top")
    app.create_text("Type the name of the application/s you would like to kill", "top")
    app.create_button("Kill Application's")

    # Keeps window 'alive'; without this the window instantly closes.
    app.mainloop()