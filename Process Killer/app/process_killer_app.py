import tkinter as tk
from app.app_state import AppState

# Title, Icon, Window size (Width x Length)
title = "Process Killer"
icon_path = ""
window_size = "320x480"

# Create "Application State"
sstate = AppState()

class ProcessKillerApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.placeWidgets()

    """ Design's the widgets that will beused in the GUI """
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

        # Give the user a status update
        self.current_activity = tk.Label()
        self.current_activity["text"] = "Current Activity display (searching/killing)"

        # Display stats to the user about how many processes were found that were relevant and how many were killed
        self.killed_information = tk.Label()        
        self.killed_information["text"] = "000 / 000 processes killed"

    """ Places widgets in order on the GUI window"""
    def placeWidgets(self):
        self.instruction_label.pack()
        self.process_name_to_kill.pack()
        self.submit_process_name.pack()
        self.current_activity.pack()
        self.killed_information.pack()
    
    # TODO: Set process name to state & trigger scanner
    """ Triggered by the 'submit_process_information' button
        It sets the process name in app/state_info.
        Triggers the scanner function.
        While the scanner passes data to the Queue, processes with the name in state will be killed"""
    def get_process_to_kill(self):
        process_name = self.process_name_to_kill.get().lower()
        sstate.set_name(process_name)
        

# Instantiate the Window & Application GUI
root = tk.Tk()
root.geometry(window_size)
app = ProcessKillerApp(master=root)
app.mainloop()