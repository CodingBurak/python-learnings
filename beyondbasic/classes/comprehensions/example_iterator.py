class MyIterator:
  def __init__(self, values) -> None:
    self.index = 0
    self.values = values
    
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.index >= len(self.values):
      raise StopIteration()
    res = self.values[self.index]
    self.index += 1
    return res
  
  
class MyIterable:
  def __init__(self,data) -> None:
    self.data = data
    
  def __iter__(self):
    return MyIterator(self.data)