import sys
import os
import random
import tkinter as tk
import time

from .app_state import state
from .scan_processes import scanner
from .kill_from_queue import killer


class ProcessKillerApp(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()
        self.place_widgets()
        self.update_widgets()

    def create_widgets(self):
        """ Design's the widgets that will beused in the GUI """

        # Give the user a status update, by default this instructs the user enter an application name
        self.current_action_text = tk.StringVar()
        self.current_action = tk.Label()
        self.current_action["textvariable"] = self.current_action_text

        # Input to let the user give us a process name
        self.process_name_to_kill = tk.Entry()

        # Button for submitting the process name to be killed
        self.submit_process_name = tk.Button()
        self.submit_process_name["text"] = "Kill Processes!"
        self.submit_process_name["command"] = self.onClick_submit_process

        # Display stats to the user about how many processes were found that were relevant and how many were killed
        self.scan_counter_text = tk.StringVar()
        self.scan_counter = tk.Label()
        self.scan_counter["textvariable"] = self.scan_counter_text

    def place_widgets(self):
        """ Places widgets in order on the GUI window"""
        self.current_action.pack()
        self.process_name_to_kill.pack()
        self.submit_process_name.pack()
        self.scan_counter.pack()

    def update_widgets(self):
        print("Updating Widgets")

        # Update current action
        activity = f"{state.get_current_action()}..."
        self.current_action_text.set(activity)

        # Update process scan counter
        scan_counter = f"{state.get_processes_scanned_count()} processes scanned"
        self.scan_counter_text.set(scan_counter)

    def force_update(self):
        """ Triggers a widget update, then forces an update of idle tasks (ie like a widget update)
            this allows us to tell the user whats happening in the application at any given moment"""
        print("Forced update")
        self.update_widgets()
        self.master.update_idletasks()

    def onClick_submit_process(self):
        """ Triggered by the 'submit_process_information' button
            It sets the process name in app/state_info.
            Triggers the scanner function.
            Triggers killer function"""

        # This prevents a double-click slowing freezing the application
        while state.get_has_scanned() is False:
            # Gets the process name from the textbox in all lowercase
            process_name = self.process_name_to_kill.get().lower()

            # Sets the name in the application state
            if len(process_name) == 0:
                print("app name too small")
                # Case: The user hit enter or submit without typing anything
                break
            state.set_name(process_name)
            print("starting application scripts")

            # Sets current_action, update's widgets, calls scanner, updates idle tasks
            print("setting state and calling scanner")
            state.set_current_action("Scanning for processes")
            self.force_update()
            print(state.get_current_action())
            scanner()
            self.force_update()

            # Sets current_action, updates widgets, kills applications from queue
            print("setting state and calling killer")
            state.set_current_action("Killing processes")
            print(state.get_current_action())
            self.force_update()
            killer()

            # Sets current_action, updates widgets
            state.set_current_action("Enter another process or application name")
            self.force_update()

            # Call set_has_scanned(), setting the value to true and ending the loop
            state.set_has_scanned()
        #TODO: notify the user with a pop-up to "wait" or to re-start the application
        else:
            pass



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
