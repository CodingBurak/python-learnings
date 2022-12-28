class LoggingContextManager:
  
  def __enter__(self):
    print("enntered")
    return self
  
  def __exit__(self, exc_type, exc_val, exc_tb):
    if exc_type is None:
      print("normal exit")
    else:
      print("lcm exit type {} value {} tb{}".format(exc_type, exc_val, exc_tb))

