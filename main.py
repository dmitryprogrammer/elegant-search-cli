import sys
from src.filename import getFileName

fileName = getFileName()
searchString = len(sys.argv) > 2 and sys.argv[2] or None

if not fileName:
    fileName = input("Please enter filename: ")

with open(fileName, "r") as f:
    f.seek(0)
    fileContent = f.read()
    if searchString:
        hasSearchString = fileContent.find(searchString) >= 0
    else:
        hasSearchString = False

    if hasSearchString:
        print("Search string found in file")
    else:
        print("Search string not found in file")
