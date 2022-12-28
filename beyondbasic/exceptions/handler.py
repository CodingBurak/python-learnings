from random import randrange
import math
import sys
import traceback
def main():
  number = randrange(100)
  
  while True:
    try:
      guess = (int(input("??? ")))
    except ValueError:
      continue
    if guess == number:
      print("well domne")
      break
    
def loopup():
  s = [1,2,3]
  try: 
    item = s[4]
  except IndexError:
    print("handle error", IndexError.mro())
    
  d= dict(a=4, b = 3)
  try:
    item = d["s"]
  except LookupError:
    print("handleerror")
    
class TriangleError(Exception):

  def __init__(self, text, sides) -> None:
    super().__init__(text)
    self._sides = tuple(sides) #immutable!
  
  @property
  def sides(self):
    return self._sides 
  
  def __str__(self) -> str:
    return "'{}' for sides {}".format(self.args[0], self.sides)
  
  def __repr__(self):
    return "TriangeError({!r}, {!r}".format(self.args[0], self.sides)
    
def triangle(a,b,c):
  sides = sorted((a,b,c))
  if sides[2] > sides[0] +sides[1]: raise TriangleError("illegal triangel", sides)
  p = (a+b+c) /2
  a = math.sqrt(p*(p-a)* (p-b) * (p-c))
  return a


def main():
  try:
    a = triangle(3,4,10)
    print(a)
  except TriangleError as e:
    print(e, file=sys.stdin) # will throw another exception like During handling of the above exception, another exception occurred: 
    #__context__ is holding the triangle error
    
class InclinationError(Exception):
  pass

def inclination(deltax, deltay):
  try:
    return math.degrees(math.atan(deltay / deltax))
  except ZeroDivisionError as e:
    raise InclinationError(" my exception") from e# associates the new exceptional object with the original excepion e, __cause__

if __name__ == "__main__":
  try:
    inclination(0,10)
  except InclinationError as e:
    print(e)
    print(e.args)
    print(e.__context__)
    print(e.__cause__)
    print(e.__traceback__)
    traceback.print_tb(e.__traceback__)
  print("FINISHED")
  