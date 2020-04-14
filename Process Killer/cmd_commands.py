"""Running this command in an un-elevanted command prompt will give you a readout of
Process Name's (caption), File Location (commandline) & PID's (processid)
"""
get_proc = "WMIC PROCESS GET caption, commandline, processid"