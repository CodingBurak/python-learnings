class Base:
  helloBase = "ho"
  def __init__(self):
    print("innit base called")
    
  def f(self):
    print("base f is called")
    
  
  
class Sub(Base):
  
  def __init__(self):
    super().__init__()
    print("sub innit called")
  def f(self):
    print("sub f")