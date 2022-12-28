def check_non_negative(index):
  def validator(f):
    def wrapper(*args, **kwargs):
      if args[index] < 0:
        raise ValueError("negative number")
      return f(*args, **kwargs)
    return wrapper
  return validator

@check_non_negative(5)
def generate_list(value, size):
  return [value] * size

