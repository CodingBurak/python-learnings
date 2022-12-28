class SimpleList:
  def __init__(self, items) -> None:
    self.items = list(items)
    
  def add(self, item):
    print("in Simpple add")
    self.items.append(item)
    
  def __getitem__(self, index):
    return self.items[index]
  
  def sort(self):
    return self.items.sort()
  
  def __len__(self):
    return len(self.items)
  
  def __repr__(self):
    return "SimpleList({!r})".format(self.items)
  
class IntermediateList(SimpleList):
  
  def add(self, item):
    print("in intermediary add")
    return super().add(item)
  
  
class SortedList(IntermediateList):
  
  def __init__(self, items=()) -> None:
    super().__init__(items)
    self.sort()
  
  #override the add method
  def add(self, value):
    print("in Sorted add")
    super().add(value)
    self.sort()
    
  def __repr__(self):
    return "SortedList({!r})".format(self.items)
  
  
class IntList(SimpleList):
  def __init__(self, items):
    for x in items: self.validate(x)
    super().__init__(items)
  
  @staticmethod
  def validate(x):
      if not isinstance(x, int):
        raise TypeError("IntList doesnt supp int values")  
      
  def add(self, item):
      print("in INT add")
      self.validate(item)
      super().add(item)
        
  def __repr__(self):
    return "IntList({!r})".format(self.items)
  

class SortedIntList(IntList, SortedList ):
 
  def __init__(self, items):
    super().__init__(items)
        
  def __repr__(self):
    return "SortedIntList({!r})".format(self.items)
    
        
class SetList(SimpleList):
  def __init__(self, items) -> None:
   self.items = set(items)
   
  def add(self, value):
    self.items.add(value)
  
  def __repr__(self):
    return "SetList({!r})".format(self.items)