""" This script scan's running processes on a WINDOWS machine, then filters the data and passes it to a Queue
    scanner()
        - Scans the running processes
        - Each process is a process string
        -   for each process we pass it to the string processor

    string_processor(process)
        - Takes in an individual process string of an UNKNOWN length
        - Captures and sets the process name from the string by looping from the beginning of the string
        - Captures and sets the process id from the string by looping backwards
            - reverses the backwards process id
        
        - Creates a dict (bucket) and passes it to the state's queue
    """

import subprocess
from .app_state import state

# Returns a "list" of running processes in a Command Prompt shell on Windows, parsable by subprocess.Popen()
cmd_command = "WMIC PROCESS GET caption, commandline, processid"

""" Scans the windows system for running processes
    compares each process running to see if the application_name from state can be found
    if it is found, we pass it to string_processor """
def scanner():
    print("\nScanner Started\n")
    state.increment_process_scanned_count()

    # TODO: Define what the fuck that script from the 1 hour long bug hunt does to solve the Popen issue.
    """ IDK WHAT THIS DOES"""
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    processes = subprocess.Popen(cmd_command, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
       
    for process in processes.stdout:
        lowercase_process_str = process.decode('utf-8').lower()
        name_in_state = state.get_name()
        state.increment_process_scanned_count() # Helps keep track of the number of processes scanned

        # print(lowercase_process_str)

        if len(process.strip()) is 0:
            pass

        # If the application name the user entered is found as a sub-string in the process sting pass it to the string_processor
        if name_in_state in lowercase_process_str:
            string_processor(process.decode('utf-8'))


    print("\nScanner Ended\n")

""" Formats given 'process' string to extract a process name and process id
    passes that info as a dictionary to a Queue """
def string_processor(process):
    name_found = False
    name_list = []
    pid_found = False
    pid_list = []

    # traverse the string from the beginning for Name
    if name_found is False:
        for i in range(len(process)):

            # We know we finished adding the first string when we encounter 2 spaces in a row
            if process[i] == ' ':
                if process[i+1] == ' ':
                    name_found = True
                    break
            
            name_list.append(process[i])
            
    # traverse the string from the end for pid
    if pid_found is False:
        temp_list = []
        fail_safe = 0
        for i in range(len(process)):

            index = ((len(process) - 1) - i) # End of the string's length, then -1 everytime we loop

            # If the current index is a space & the next index is a space we continue
            if process[index] == ' ':
                if process[index-1] == ' ':
                    continue

            """ We are implementing a "fail_safe" system to make sure we only add the PID (Process Id).
                The end of a pid string should look similar to this (since we are moving thorugh groups of spaces above)
                ...iles/adobe/cc.exe" -fullscreen -vol100 53425325 "

                take note of how there is a space at the end of the string & before the process id starts " 53425325 "

                those spaces notate the beginning and end of the string.

                The fail_safe system has three values, 0, 1, 2

                0 if the default state and what allows us to start adding parts of the pid

                when we start at the space at the end of the pid, converting to an integer produces a ValueError.
                    If the fail_safe is not 2, we set the fail_safe to 1

                when the character can be converted to an integer, we add the number to the list & we reverse it later

                when we get another value error and the fail_safe is set to 1
                    we set the fail_safe equal to 2
                    mark the pid as found
                    break the loop since we are done
            """
            try:
                int(process[index])
                if fail_safe is 1:
                    temp_list.append(process[index])
            except ValueError:
                if process[index] == ' ':
                    if fail_safe is not 2: 
                        fail_safe = 1
                        continue
                else:
                    if fail_safe is 1:
                        pid_found = True
                        fail_safe = 2
                        break
            
                        
        # Loop over the temp list and basically reverse it for pid_list
        for i in range(len(temp_list)):
            # Pop the last item and add it to pid list
            last_item = temp_list.pop(len(temp_list)-1)
            pid_list.append(last_item)

    # Convert the list's to strings
    process_name = ''.join(name_list)
    process_id = ''.join(pid_list)
    bucket = {
        'name': process_name,
        'pid': process_id
    }
    
    state.add_to_queue(bucket)