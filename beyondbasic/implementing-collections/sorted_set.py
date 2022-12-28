from collections.abc import Sequence, Set, MutableSet
from bisect import bisect_left
from itertools import chain

class SortedSet(Sequence, MutableSet):
  
  def __init__(self, items=None):
    self.items = sorted(set(items)) if items is not None else []
    
  def __contains__(self, item):
    index = bisect_left(self.items, item)
    return (index != len(self.items)) and (self.items[index] == item)
  
  def __len__(self):
    return len(self.items)
  
  def __iter__(self):
    return iter(self.items)

  def __getitem__(self, index):
    result = self.items.__getitem__(index)
    return SortedSet(result) if isinstance(index, slice) else result
  
  def __repr__(self) -> str:
    return "SortedSet({})".format(repr(self.items) if self.items else "")
  
  def __eq__(self, rhs):
    if not isinstance(rhs, SortedSet):
      return NotImplemented
    return rhs.items == self.items
  
  def __ne__(self, rhs: object) -> bool:
    if not isinstance(rhs, SortedSet):
      return NotImplemented
    return rhs.items != self.items

  def count(self, item):
    return int(item in self.items) #calls the contain
  
  def index(self, item) -> int:
    index = bisect_left(self.items, item)
    print("index", index)
    if (index != len(self.items)) and (self.items[index] == item): return index
    raise ValueError()
  
  def __add__(self, rhs):
    return SortedSet(self.items + rhs.items)
  
  def add(self, rhs):
    self.items.append(rhs)
    return self
  
  def discard(self, value) -> None:
    self.items.remove(value)
    return self
  
  def __mul__(self, rhs):
    return SortedSet(self.items * rhs)
  
  def __rmul__(self, lhs):
    return self * lhs
  
  def issubset(self, iterable):
    return self <= SortedSet(items=iterable)
  
  def issuperset(self, iterable):
    return self >= SortedSet(iterable)
  
  def intersection(self, iterable):
    return self & SortedSet(iterable)
  
  def union(self, iterable):
    return self | SortedSet(iterable)
  
  def symmetric_difference(self, iterable):
    return self ^ SortedSet(iterable)
  
  def difference(self, iterable):
    return self -SortedSet(iterable)  
  