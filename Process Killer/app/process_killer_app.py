import tkinter as tk

# Title, Icon, Window size (Width x Length)
title = "Process Killer"
icon_path = ""
window_size = "350x400"

class ProcessKillerApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.placeWidgets()

    def createWidgets(self):
        # Label for instructing user what the hell to do
        self.instruction_label = tk.Label()
        self.instruction_label["text"] = "Enter the name of a process or application to kill."

        # Input to let the user give us a process name
        self.process_name_to_kill = tk.Entry()

        # Button for submitting the process name to be killed
        self.submit_process_name = tk.Button()
        self.submit_process_name["text"] = "Kill Processes!"
        self.submit_process_name["command"] = self.get_process_to_kill

    def placeWidgets(self):
        self.instruction_label.pack()
        self.process_name_to_kill.pack()
        self.submit_process_name.pack()
    
    # Get the name of the process to kill
    def get_process_to_kill(self):
        print("lol")
        

# Instantiate the Window & Application GUI
root = tk.Tk()
root.geometry(window_size)
app = ProcessKillerApp(master=root)
app.mainloop()