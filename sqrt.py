import sys
def sqrt(x):
  if( x < 0):
    raise ValueError("negative", x)
  try:
    guess = x
    i=0
    while guprintess * guess != x and i < 1000:
      guess = (guess + (x / guess))/2 
      i+=1
    return guess
  except ZeroDivisionError:
    print("error")
    return 0


def main():
  print(sqrt(9))
  print(sqrt(2))
  try:
    print(sqrt(-1))
  except ValueError as e:
    print(e, file=sys.stderr)
  
if __name__ == 'main':
  main()]