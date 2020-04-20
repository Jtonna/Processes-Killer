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
    """
    for process in processes_shell.stdout:
        processes_scanned =+ 1

        # Filter out process killer & varients from the results
        if "Process Killer" in process or "Process_Killer" in process:
            continue

        print(process)  


scanner()



