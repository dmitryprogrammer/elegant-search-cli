import sys

pathBase = "./data/"
filename = pathBase + sys.argv[1]
sought = sys.argv[2:]

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        print("line - ", line.strip())