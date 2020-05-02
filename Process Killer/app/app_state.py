import warnings
from .dll_queue.queue import Queue

class AppState:
    def __init__(self):
        self.application_name = None
        self.processes_scanned_count = 0
        self.q = Queue()

    """ Allows us to set the application name the user wants to kill """
    def set_name(self, application_name=None, processes_scanned=0):   
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
    
    """ Returns the application name for evaluation in the process string """
    def get_name(self):
        return self.application_name
    
    """ Increments processes_scanned by 1 everytime it gets called """
    def increment_process_scanned_count(self):
        self.processes_scanned_count = self.processes_scanned_count + 1
    
    """ Using the Queue 'q', we are able to easily add a 'bucket' of data to end of the queue """
    def add_to_queue(self, value):
        self.processes_scanned_count = self.processes_scanned_count+1
        self.q.enqueue(value)
    
    """ Using the Queue 'q', we are able to Remove & Return the first item from the queue """
    def remove_from_queue(self):
        return self.q.dequeue()

    """ Using the Queue 'q', we can monitor the length of the q; ie how many 'buckets' there are """
    def len_of_queue(self):
        return self.q.len()
   
    """ Returns the application state for debugging"""
    def get_state(self):
        # print( self.application_name, self.processes_scanned_count )
        pass

    """ This completely wipes and resets the state,
        this is useful for when the user wants to kill more than one application"""
    def _reset_state(self):
        # TODO: Implement _reset_state
        pass

# Creates the state object so it can be accesses from anywhere in the application
state = AppState()