import subprocess
from .app_state import state

def killer():
    while state.len_of_queue() > 0:

        item = state.remove_from_queue()
        command = "taskkill /F /PID "+item['pid']
        # kill_task = subprocess.run(command, capture_output=True, shell=True)
        # bytesdata = kill_task.stderr
        # ugly_string = "".join(map(chr, bytesdata))
        # err_no_access = "could not be terminated."

        # if err_no_access in ugly_string:
        #     ele_command = "ele taskkill /F /PID "+item['pid']
        #     subprocess.run(command, shell=True)
        #     print("process killed with admin")
        # else:
        #     print("process was killed regularly")

        subprocess.Popen(command, shell=True)