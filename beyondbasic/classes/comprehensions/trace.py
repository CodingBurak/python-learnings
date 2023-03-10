class Trace:
    def __init__(self) -> None:
        self.enabled = True
        
    def __call__(self, f):
        def wrap(*args, **kwargs):
          if self.enabled:
            print("Calling {}".format(f))
          return f(*args, **kwargs)
        return wrap
      
