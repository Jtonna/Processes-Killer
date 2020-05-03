import sys, os
import random
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
        self.updateWidgets()

    def createWidgets(self):
        """ Design's the widgets that will beused in the GUI """


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
        self.current_activity_text = tk.StringVar()
        self.current_activity = tk.Label()
        self.current_activity["textvariable"] = self.current_activity_text

        # Display stats to the user about how many processes were found that were relevant and how many were killed
        self.scan_counter_text = tk.StringVar()
        self.scan_counter = tk.Label()        
        self.scan_counter["textvariable"] = self.scan_counter_text

    def placeWidgets(self):
        """ Places widgets in order on the GUI window"""
        self.instruction_label.pack()
        self.process_name_to_kill.pack()
        self.submit_process_name.pack()
        self.current_activity.pack()
        self.scan_counter.pack()
    
    def updateWidgetText(self, widget_name, new_text):
        print("loop")

        current_activity = state.get_current_activity()+"..."
        self.current_activity_text.set(current_activity)

        # Update process scan counter
        scan_counter = f"{state.get_processes_scanned()} processes scanned"
        self.scan_counter_text.set(scan_counter)

        # self.widget_name.set(new_text)

        # Recursion to keep these updating
        self.master.after(5, self.updateWidgets)
    
    def get_process_to_kill(self):
        """ Triggered by the 'submit_process_information' button
            It sets the process name in app/state_info.
            Triggers the scanner function.
            While the scanner passes data to the Queue, processes with the name in state will be killed"""

        # Gets the process name from the textbox in all lowercase
        process_name = self.process_name_to_kill.get().lower()

        # Sets the name in the application state
        state.set_name(process_name)

        # Triggers the scanner function # while loop for killer
        scanner()
    

""" Everything below here is for managing the window size, icon, title and the actual window geometry """

def img_resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
# input()
# Title, Icon, Window size (Width x Length)
title = "Process Killer"
icon_path = img_resource_path("app/img/app_icon.ico")
window_width = 320
window_height = 480
window_size = str(window_width)+"x"+str(window_height)

# Create a blank 0x0px window
root = tk.Tk()

# Set icon, title and window size
root.wm_iconbitmap(icon_path)
root.title(title)
root.geometry(window_size)
root.resizable(False, False)

# Instansiate the widgets and place them
app = ProcessKillerApp(master=root)

# Main loop so the app only closes when the user clicks the close button
app.mainloop()