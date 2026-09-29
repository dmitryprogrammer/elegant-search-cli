import sys

BASE_PATH = "./data"

def getFileName():
    if(len(sys.argv) <= 1):
       return None 

    fileName = sys.argv[1]

    return BASE_PATH + "/" + fileName

__all__ = ["getFileName"]