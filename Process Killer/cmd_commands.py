"""Running this command in an un-elevanted command prompt will give you a readout of
Process Name's (caption), File Location (commandline) & PID's (processid)
"""
get_proc = "WMIC PROCESS GET caption, commandline, processid"

"""This command uses taskkill to kill tasks, task kill has several parameters even Admin kill, which could be usefull
https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/taskkill
"""
kill_proc = "taskkill /F /PID "