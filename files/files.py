import sys

def main(filename):
  with open(filename, mode ="rt") as f:
    return [int(line) for line in f]
    
if __name__ == "__main__":
  main(sys.argv[1])