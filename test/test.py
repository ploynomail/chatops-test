#!/bin/python
import os

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    print("Hello World!")
    print(os.getcwd())
    print(os.abc)
    print("hee")
if __name__ == "__main__":
    main("s")