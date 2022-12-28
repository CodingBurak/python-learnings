def custom_endswith(d, list_end):
    for end_pattern in list_end:
        if d.endswith(end_pattern):
            return True
    return False
  
def start():
  
  list_end = ["=",";",")","("]
  list_variable = []

  data = ["int zt;",
    "public int w = 3;",
    "public final int nu;public a(d dVar, int i, int i2);",
    "public int getScoreOrder() {int getInteger;",
    "for (int i = 0; i < this.nu; i++)",
    "{public a(d dVar, int t) {super(dVar, i);",
    "private int z = true ;if (getType() != 1) {z = false;",
    "protected int g = true;",
    "unprotected int z = true;if (getType() != 1) {z = false;",
    "public int getType() {return getInteger();",
    "int y;",
    "print (int i) {int k = b.k(parcel);"]

  for d in data:
      splitted = d.split(";")
      for semic in splitted:
        found = semic.find("int")
        print("index2", found)
        if found is not None and custom_endswith(semic, list_end):
            list_variable.append(semic[found + len("int"):-1])
  print(list_variable)
  
start()

