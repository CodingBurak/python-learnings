def is_even(x):
  if x % 2 == 0:
    return True
  return False

c = [x for x in range(100) if is_even(x)]

def get_first(iterable):
  try:
    iterator = iter(iterable)
    return next(iterator)
  except StopIteration:
    raise ValueError("end of iterable")
  
def take(amount, iterable):
  counter = 0
  
  for item in iterable:
    print("counter", counter)
    if(counter == amount):
      return
    counter+=1
    print("about to yield in take", item)
    #after yielding it will go inside callee
    yield item
    
def run_take():
  iterable_arr = [1,2,3,4,5,6]
  #will take each yield item on demand, counter will be stateful as it holds the value and is nor regenerated!
  item =  take(4, iterable_arr)
  return item

def distinct(iterable):
  seen = set()
  for item in iterable:
    if item in seen:
      print("in continue distinct")
      continue
    seen.add(item)
    print("about to yield in distinct", item)
    yield item
    
def run_distinct():
  items = [1,1,4,4,3,2,1,3]
  
  for item in distinct(items):
    print(item)
    
def run_pipeline():
  items = [1,1,4,4,3,1,3]
  for item in take(4, distinct(items)):
    print("item", item)
if __name__ == "__main__":
  run_pipeline()
  