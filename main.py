import sys

def main():
    fileName = sys.argv[1]
    search = sys.argv[2:]
    print(fileName, *search)

main()