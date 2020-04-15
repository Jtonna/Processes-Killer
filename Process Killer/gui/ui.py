import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    


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

    # Keeps window 'alive'; without this the window instantly closes.
    app.mainloop()