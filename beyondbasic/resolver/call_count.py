class ClassCounter:
  
  def __init__(self, f):
    print("inn init")
    self.f = f
    self.count = 0
  
  def __call__(self,*args, **kwargs):
    print("in call")
    self.count +=1
    print("couter", self.count)
    return self.f(*args, **kwargs)

  
@ClassCounter
def to_instance():
  print("in toinstance method")