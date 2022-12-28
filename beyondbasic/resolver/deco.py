def splice_deco(f):
    def wrapper( *args, **kwargs):
      shortened = f(*args, **kwargs)
      return shortened[:-1]
    return wrapper

#@splice_deco
def print_string(param):
  return param

