import sys

BASE_PATH = "./data"

def getFileName(inputFileName=None):
    if inputFileName:
        fileName = inputFileName
    elif len(sys.argv) > 1:
        fileName = sys.argv[1]
    else:
        return None

    return BASE_PATH + "/" + fileName

__all__ = ["getFileName"]