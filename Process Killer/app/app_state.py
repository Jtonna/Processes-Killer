import warnings
from .dll_queue.queue import Queue

class AppState:
    def __init__(self):
        self.application_name = None
        self.processes_scanned_count = 0
        # self.relevant_processes = relevant_processes
        # self.processes_killed = processes_killed
        # self.processes_failed = processes_failed
        self.q = Queue()

    """ Allows us to set the application name we want to kill """
    def set_name(self, application_name=None, processes_scanned=0):   
        # TODO: Setup logger for all the print statements below
        print(f"\n\n*****\nIncoming name: {application_name}, Previous name: {self.application_name}\n")        
        # Case: User double clicked the kill button
        if self.application_name == application_name:
            print("\nNameWarning @app_state.py:\n   Incoming name is the same as name in state")
            pass
        # Case: Trying to kill a new application
        elif self.application_name != None:
            # TODO: The user May be trying to kill another application, we need to handle this somewhere else
            print(f"\nNameWarning @app_state.py:\n    Error attempting to kill another application: '{application_name}', please close and re-open the application")
        # Case: There is no name set, so we set one
        else:
            print("\nNameWarning @app_state.py:\n   Setting application name for the first name")
            self.application_name = application_name
    
    """ Returns the application name for evaluation in the process string """
    def get_name(self):
        return self.application_name
    
    """ Increments processes_scanned by 1 everytime it gets called """
    def increment_process_scanned_count(self):
        self.processes_scanned_count = self.processes_scanned_count + 1

    """ Returns the application state """
    def get_state(self):
        print(
            self.application_name, 
            self.processes_scanned_count
            # self.relevant_processes,
            # self.processes_killed,
            # self.processes_failed
        )
    
    """ Easier access to enqueueing since most modules will have access
        to app_state; i did this because im tired of random import issues """
    def add_to_queue(self, value):
        self.processes_scanned_count = self.processes_scanned_count+1
        self.q.enqueue(value)
    
    """ Easier access to dequeueing since most modules will have access
        to app_state; i did this because im tired of random import issues """
    def remove_from_queue(self):
        return self.q.dequeue()

    """ Returns the length of the queue """
    def len_of_queue(self):
        return self.q.len()

    """ This completely wipes and resets the state,
        this is useful for when the user wants to kill more than one application"""
    def _reset_state(self):
        # TODO: Implement _reset_state
        pass



# Creates the state object
state = AppState()

# s = AppState()

# s.get_state()

# s.set_name(application_name="Adobe")
# s.set_process_scanned()
# s.set_process_scanned()
# s.set_process_scanned()
# s.set_process_scanned()
# s.get_state()

# s.set_name(application_name="Slack")
# s.set_process_scanned()
# s.set_process_scanned()
# s.set_process_scanned()
# s.set_process_scanned() 
# s.get_state()

# s.add_to_queue(43)
# s.add_to_queue(433)
# s.add_to_queue(2353)

# s.remove_from_queue()
