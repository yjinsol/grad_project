import os, sys
from win32com.client import GetObject

def getProcessesList():
        PROCESS_LIST_ = []
        getObj_ = GetObject('winmgmts:')
        processes_ = getObj_.InstancesOf('Win32_Process')
        for ps_ in processes_:
            PROCESS_LIST_.append(ps_.Properties_('Name').Value)
        return PROCESS_LIST_

getProcessesList()