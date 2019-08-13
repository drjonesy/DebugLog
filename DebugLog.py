import os, sys
from datetime import datetime

def TEST(s: str=""):
    print(s)
    sys.exit()

def PAUSE(s: str=""):
    print(s)
    input()

class Log:
    INFO = 0
    DEBUG = 1
    WARNING = 2
    ERROR = 3
    CRITICAL = 4

    def __init__(self, logPath: str="", level: int=INFO):
        self.__logPath = logPath
        self.__level = level
        self.__MakeFileAndFolders()
    
    def __MakeFileAndFolders(self):
        ''' A private method. Used to create folder directory and log file.'''
        if os.path.isfile(self.__logPath): # check if file already exists
            pass
        else:
            folderPath, fileName = os.path.split(self.__logPath)
            if os.path.isdir(folderPath): # check if current directory path exist
                with open(os.path.join(folderPath, fileName), "w") as _file:
                    pass
            else:
                os.makedirs(folderPath, exist_ok=True) # create all nested directories in folderPath
                with open(os.path.join(folderPath, fileName), "w") as _file:
                    pass

                
    def msg(self, msg: str=""):
        '''Log a generic message without debug tag'''
        with open(self.__logPath, "a+") as log:
            log.write(f"{msg}\n")
            
    def info(self, msg: str=""):
        '''Log a INFO message'''
        with open(self.__logPath, "a+") as log:
            log.write(f"INFO: {msg}\n")
    
    def debug(self, msg: str=""):
        '''Log a DEBUG message'''
        if self.__level > 0:
            with open(self.__logPath, "a+") as log:
                log.write(f"DEBUG: {msg}\n")
    
    def warning(self, msg: str=""):
        '''Log a WARNING message'''
        if self.__level > 1:
            with open(self.__logPath, "a+") as log:
                log.write(f"WARNING: {msg}\n")
    
    def error(self, msg: str=""):
        '''Log a ERROR message'''
        if self.__level > 2:
            with open(self.__logPath, "a+") as log:
                log.write(f"ERROR: {msg}\n")

    def critical(self, msg: str=""):
        '''Log a CRITICAL message'''
        if self.__level > 3:
            with open(self.__logPath, "a+") as log:
                log.write(f"CRITICAL: {msg}\n")

    def Lvl(self, level: int=INFO):
        '''Change the Log Level'''
        self.__level = level
    