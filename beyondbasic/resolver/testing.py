store = []

def sort_by_last(strings):
    def last_letter(s):
      return s[-1]
    store.append(last_letter)
    return sorted(strings,key=last_letter)
  
def outer(param):
  counter = param
  print("counter", counter)
  def inner(x):
      print("inner")

      return counter +x
  return inner

