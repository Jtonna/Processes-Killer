""" Scan's running processes, Filters information and then passes the resulting data into a DLL Queue
"""

import subprocess

# Returns a "list" of running processes in a Command Prompt shell on Windows, parsable by subprocess.Popen()
cmd_command = "WMIC PROCESS GET caption, commandline, processid"

# Runs the cmd command, and allows data to be parsed
processes_shell = subprocess.Popen(cmd_command, shell=True, universal_newlines=True, stdout=subprocess.PIPE)

processes_scanned = 0

def scanner():

    """For each process in the subprocess.Popen() shell, we will
        1. filter out "Process Killer" and all possible varients of that name
        2. pass the string to a "string processor" that will get the Program Name & PID
        3. pass the returned data to the Queue
    """
    for process in processes_shell.stdout:
        processes_scanned =+ 1

        # Filter out new lines that are basically empty strings
        if len(process) < 2:
            continue

        # Filter out process killer & varients from the results
        if "Process Killer" in process or "Process_Killer" in process:
            continue
        
        # print(f"***Passing a string: {len(process)}")
        string_processor(process)


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
    print(f"name: {process_name}\npid: {process_id}\n\n")

scanner()

    
