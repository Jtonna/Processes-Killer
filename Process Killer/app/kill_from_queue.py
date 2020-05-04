""" This Module is used to kill processes by its PROCESS ID on a Windows Machine
    
    !NOTE:
    Since the application gets compiled with Pyinstallers --uac-admin & --uac-uiaccess command
    this shell is an elevated command promt; this means that
        - This shell can kill ANY application
        - When using Remote Desktop, the shell will still work"""
import subprocess
from .app_state import state
from .scan_processes import scanner

def killer():
    """ Dequeues, adds the queue item's PID to a list as a string with '/pid ' appended to the beginning.
        Then merges the list into a string, and runs the taskkill command to kill all the tasks at once
        
        !WARNING: If a task that has spawned a process child is killed, they will all be terminated as well;
        This produces an 'ERROR: The process xxxx not found' that we can just ignore."""

    pid_kill_list = []
    pid_string = ""
    task_kill_command = "taskkill /F "
    # https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill#parameters

    # Populate the pid kill_list
    while state.len_of_kill_queue() > 0:
        queue_item = state.remove_from_kill_queue()
        pid_kill_list.append(f"/pid {queue_item['pid']} ")

    # Traverse the kill_list and create a string with all pids
    for pid in pid_kill_list:
        pid_string += pid

    # If the kill list contains pid's and commands, kill them all at once
    cmd = task_kill_command+pid_string
    subprocess.Popen(cmd, shell=True)
    print(f"Ran following command in shell:{cmd}")