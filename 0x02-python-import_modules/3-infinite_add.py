#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    k = 0
    for i in range(1,len(argv)):
        k += int(argv[i])
    print("{}".format(k))
