""" This module/class contains the application 'state', 
    such as all of the data created by running processes
    and what is currently happening in the application """

import warnings
from .dll_queue.queue import Queue


class AppState:
    def __init__(self):
        self.current_action = "Enter the name of a process or application"
        self.application_name = None
        self.has_scanned_and_killed = False
        self.processes_scanned_count = 0
        self.unprocessed_strings_q = Queue()
        self.kill_q = Queue()

    def set_current_action(self, action):
        """ Allows us to set a current action so the user knows what we are doing """
        self.current_action = action

    def get_current_action(self):
        """ Returns the current action so the user knows whats going on """
        return self.current_action

    def set_name(self, application_name=None):
        """ Allows us to set the application name the user wants to kill """
        # TODO: Setup logger for all the print statements below
        # print(f"\n\n*****\nIncoming name: {application_name}, Previous name: {self.application_name}\n")
        # Case: User double clicked the kill button
        if self.application_name == application_name:
            # print("\nNameWarning @app_state.py:\n   Incoming name is the same as name in state")
            pass

        # TODO: Implement _reset_state when the user enters a new application name
        # Case: Trying to kill an application with a different name
        elif self.application_name != None:
            # TODO: The user May be trying to kill another application, we need to handle this somewhere else
            print(
                f"\nNameWarning @app_state.py:\n    Error attempting to kill another application: '{application_name}', please close and re-open the application")

        # Case: There is no name set, so we set one
        else:
            # print("\nNameWarning @app_state.py:\n   Setting application name for the first name")
            self.application_name = application_name

    def get_name(self):
        """ Returns the application name for evaluation in the process string """
        return self.application_name

    def set_has_scanned_and_killed(self):
        """ Sets a has_scanned_and_killed to True to help determine if we have already scanned for running processes """
        if self.has_scanned_and_killed is False:
            self.has_scanned_and_killed = True
        else:
            self.has_scanned_and_killed = False

    def get_has_scanned_and_killed(self):
        """ Returns the has_scanned_and_killed boolean """
        return self.has_scanned_and_killed

    def increment_process_scanned_count(self):
        """ Increments processes_scanned by 1 everytime it gets called """
        self.processes_scanned_count = self.processes_scanned_count + 1

    def get_processes_scanned_count(self):
        """ Returns the total number of processes scanned """
        return self.processes_scanned_count

    def add_to_unprocesses_strings_queue(self, value):
        """ Using the Queue 'unprocesses_strings_q' we are able to quickly add un-processed strings from the scanner function"""
        self.unprocessed_strings_q.enqueue(value)

    def len_of_unprocesses_strings_queue(self):
        """ Allows us to monitor the length of the unprocessed_strings Queue"""
        return self.unprocessed_strings_q.len()

    def remove_from_unprocesseed_strings_queue(self):
        """ Removes an unprocessed string queue so that it may be processed and the PID and Process Name can be added to the kill queue"""
        return self.unprocessed_strings_q.dequeue()
    
    def add_to_kill_queue(self, value):
        """ Using the Queue 'kill_q', we are able to easily add a 'bucket' of data to end of the queue, we also keep track of how many processes were added to the kill queue """
        self.processes_scanned_count = self.processes_scanned_count+1
        self.kill_q.enqueue(value)

    def len_of_kill_queue(self):
        """ Using the Queue 'kill_q', we can monitor the length of the q; ie how many 'buckets' there are """
        return self.kill_q.len()

    def remove_from_kill_queue(self):
        """ Using the Queue 'q', we are able to Remove & Return the first item from the queue """
        return self.kill_q.dequeue()

    def _reset_state(self):
        """ This method resets parts of the application state required for
            killing more than one application"""
        
        # Empty out the kill queue
        while self.len_of_kill_queue() > 0:
            self.remove_from_queue()
        
        # Empty out the unprocesses strings queue
        while self.len_of_unprocesses_strings_queue() > 0:
            self.remove_from_unprocesseed_strings_queue()

        # Reset's variables
        self.has_scanned_and_killed = False
        self.application_name = None


# Creates the state object so it can be accesses from anywhere in the application
state = AppState()
