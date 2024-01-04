#!/usr/bin/python3
if __name__ == "__main__":
  from sys  import argv
  leng = len(argv) - 1
  if leng < 1:
        print("{} arguments.".format(leng))
  elif leng == 1:
        print("{} argument:".format(leng))
  else:
        print("{} arguments:".format(leng))
  for k in range(leng):
        print("{}: {:s}".format(k + 1, argv[k + 1]))
  
