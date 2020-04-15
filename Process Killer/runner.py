from gui import ui

root = ui.tk.Tk()
app = ui.Application(master=root)
root.iconbitmap("gui/img/app_icon.ico")
app.master.title("Application Killer")
app.master.minsize(400,400)
app.master.maxsize(400,400)
app.mainloop()