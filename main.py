from src.filename import getFileName

fileName = getFileName()

if(not fileName):
    print("Please enter filename")

print(fileName or "")