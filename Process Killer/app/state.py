import warnings
class AppState:
    def __init__(self):
        self.application_name = None
        self.processes_scanned = 0
        # self.relevant_processes = relevant_processes
        # self.processes_killed = processes_killed
        # self.processes_failed = processes_failed

    """ Allows us to set the application name we want to kill """
    def set_name(self, application_name=None, processes_scanned=0):       
        # Case: User double clicked the kill button
        if self.application_name is application_name:
            pass
        # Case: Trying to kill a new application
        elif self.application_name is not None:
            # TODO: The user May be trying to kill another application, we need to handle this somewhere else
            warnings.warn(f"Error attempting to kill another application: '{application_name}', please close and re-open the application", FutureWarning)
        # Case: There is no name set, so we set one
        else:
            self.application_name = application_name
        
    """ Increments processes_scanned by 1 everytime it gets called """
    def set_process_scanned(self):
        # TODO: Implement set_process_scanned in scan_processes.py
        self.processes_scanned = self.processes_scanned+1

    """ Returns the application state """
    def get_state(self):
        print(
            self.application_name, 
            self.processes_scanned
            # self.relevant_processes,
            # self.processes_killed,
            # self.processes_failed
        )

s = AppState()
s.get_state()

s.set_name(application_name="Adobe")
s.set_process_scanned()
s.set_process_scanned()
s.set_process_scanned()
s.set_process_scanned()
s.get_state()

s.set_name(application_name="Slack")
s.set_process_scanned()
s.set_process_scanned()
s.set_process_scanned()
s.set_process_scanned() 
s.get_state()