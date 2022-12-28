import time

def make_timer():
  last_time = None
  
  def elapsed_time():
    now = time.time()
    nonlocal last_time
    if last_time is None:
      last_time = now
      return None
    result = now - last_time
    last_time = now
    return result
  return elapsed_time