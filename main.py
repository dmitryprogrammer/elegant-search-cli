import sys

pathBase = "./data/"
filename = pathBase + sys.argv[1]
sought = sys.argv[2:]

with open(filename, "w+", encoding="utf-8") as file:
    for line in range(5):
        file.write(f"line${str(line)} \n")

    file.seek(0)

    for line in file:
        print("line - ", line.strip())
