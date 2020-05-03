""" This Module is used to kill processes by its PROCESS ID on a Windows Machine
    Once killer () is called, while the queue has information in it will 
        - Dequeue the bucket
        - Use Popen to spawn a new Command Prompt
        - Use 'taskkill' to kill the process by PID
    
    !NOTE:
    Since the application gets compiled with Pyinstallers --uac-admin & --uac-uiaccess command
    this shell is an elevated command promt; this means that
        - This shell can kill ANY application
        - When using Remote Desktop, the shell will still work"""
import subprocess
from .app_state import state

def killer():
    state.set_current_activity("Killing processes")
    while state.len_of_queue() > 0:

        item = state.remove_from_queue()
        command = "taskkill /F /PID "+item['pid']
        subprocess.Popen(command, shell=True)
    
    state.set_current_activity("Waiting for user inputt")