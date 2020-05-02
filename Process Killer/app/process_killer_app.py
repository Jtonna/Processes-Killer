import tkinter as tk

from .app_state import state
from .scan_processes import scanner
from .kill_from_queue import killer

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
    
    """ Triggered by the 'submit_process_information' button
        It sets the process name in app/state_info.
        Triggers the scanner function.
        While the scanner passes data to the Queue, processes with the name in state will be killed"""
    def get_process_to_kill(self):

        # Gets the process name from the textbox in all lowercase
        process_name = self.process_name_to_kill.get().lower()

        # Sets the name in the application state
        state.set_name(process_name)

        # Triggers the scanner function # while loop for killer
        scanner()
        killer()
    
""" Everything below here is for managing the window size, icon, title and the actual window geometry """

# Title, Icon, Window size (Width x Length)
title = "Process Killer"
icon_path = "app/img/app_icon.ico"
window_width = 320
window_height = 480
window_size = str(window_width)+"x"+str(window_height)

# Create a blank 0x0px window
root = tk.Tk()

# Set icon, title and window size
root.iconbitmap(icon_path)
root.title(title)
root.geometry(window_size)
root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)

# Instansiate the widgets and place them
app = ProcessKillerApp(master=root)

# Main loop so the app only closes when the user clicks the close button
app.mainloop()