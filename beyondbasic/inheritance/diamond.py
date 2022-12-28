class A:
  def func(self):
    print("A")

class B(A):
  def func(self):
    print("B")

class C(A):
  def func(self):
    print("C")
    
class D(B, C):
  pass
    
