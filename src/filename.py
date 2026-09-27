import sys

BASE_PATH = "./data"

def getFileName():
    fileName = sys.argv[1]
    
    if(not fileName):
       print("Please enter the filename")
       return

    return BASE_PATH + "/" + fileName

__all__ = ["getFileName"]