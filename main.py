from src.filename import getFileName

fileName = getFileName()

if not fileName:
    fileName = input("Please enter filename: ")

print(fileName or "no")