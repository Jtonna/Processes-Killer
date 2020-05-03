import warnings
from .dll_queue.queue import Queue

class AppState:
    def __init__(self):
        self.current_action = "Enter the name of a process or application"
        self.application_name = None
        self.has_scanned = False
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
            print(f"\nNameWarning @app_state.py:\n    Error attempting to kill another application: '{application_name}', please close and re-open the application")

        # Case: There is no name set, so we set one
        else:
            # print("\nNameWarning @app_state.py:\n   Setting application name for the first name")
            self.application_name = application_name

    def get_name(self):
        """ Returns the application name for evaluation in the process string """
        return self.application_name

    def set_has_scanned(self, boolean):
        """ Sets a has_scanned to True to help determine if we have already scanned for running processes """
        if self.has_scanned is False:
            self.has_scanned = True
    
    def get_has_scanned(self):
        """ Returns the has_scanned boolean """
        return self.has_scanned

    def increment_process_scanned_count(self):
        """ Increments processes_scanned by 1 everytime it gets called """
        self.processes_scanned_count = self.processes_scanned_count + 1
    
    def get_processes_scanned_count(self):
        """ Returns the total number of processes scanned """
        return self.processes_scanned_count

    def add_to_kill_queue(self, value):
        """ Using the Queue 'q', we are able to easily add a 'bucket' of data to end of the queue """
        self.processes_scanned_count = self.processes_scanned_count+1
        self.kill_q.enqueue(value)

    def len_of_kill_queue(self):
        """ Using the Queue 'q', we can monitor the length of the q; ie how many 'buckets' there are """
        return self.kill_q.len()

    def remove_from_kill_queue(self):
        """ Using the Queue 'q', we are able to Remove & Return the first item from the queue """
        return self.kill_q.dequeue()

    
    def _reset_state(self):
        """ This completely wipes and resets the state,
            this is useful for when the user wants to kill more than one application"""
        # TODO: Implement _reset_state
        pass

# Creates the state object so it can be accesses from anywhere in the application
state = AppState()