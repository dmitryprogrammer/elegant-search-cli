import sys

BASE_PATH = "./data"

def getFileName(inputFileName=None):
    if not inputFileName and len(sys.argv) <= 1:
        return None 
    elif not inputFileName:
        fileName = sys.argv[1]
    else:
        fileName = inputFileName

    return BASE_PATH + "/" + fileName

__all__ = ["getFileName"]