from contextlib import contextmanager

@contextmanager
def logging_ctx_manager():
  print("logging enter")
  try:
    yield "your are in a with block"
    print("logging normal exit")
  except Exception:
    print("exceptionnal exit")
    raise

@contextmanager
def file_handler(file_name, file_mode):
  my_file = open(file_name, file_mode)
  yield my_file
  my_file.close()
  
#vs classic:

class MyFileHandler():
  def __init__(self,file_name, file_mode) -> None:
    self.file = None
    self.file_name = file_name
    self.file_mode = file_mode
    
  def __enter__(self):
    print("---entered---")
    self.file = open(self.file_name, self.file_mode)
    return self.file
  
  def __exit__(self, ex_type, ex_val, ex_tb):
    self.file.close()
    if ex_type is not None: 
      print("____exited_unnormaly")
      return False
    print("____exited__normal")
    
@contextmanager
def nest_test(name):
  print("entered ", name)
  yield name
  print("exiting", name)
  
@contextmanager
def propagate(name, prop):
  try:
    print("entered ", name)
    yield name
    print(name, "exited normally")
  except Exception:
    print(name, "received an exception")
    if prop:
      raise

with propagate("first", True) as first, propagate("second", False):
  raise ValueError("an error occured in body")
  

  

