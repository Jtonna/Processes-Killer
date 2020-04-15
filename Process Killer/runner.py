from gui import ui

root = ui.tk.Tk()
app = ui.Application(master=root)
app.master.title("Application Killer")
app.master.minsize(400,400)
app.master.maxsize(400,400)
app.mainloop()