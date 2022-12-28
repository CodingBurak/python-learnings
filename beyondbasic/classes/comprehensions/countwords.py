import functools
def count_words(doc):
  normed_doc = "".join(c.lower() if c.isalpha() else " " for c in doc)
  freq = {}
  for word in normed_doc.split():
    freq[word] = freq.get(word, 0) +1
  return freq
print(count_words("asd asd as a a . da sd asd asd asda sd 213 1 2 as da sd adaaaaad asdasda asd"))

documents = ["hi my name is burak", "how are you doing", "are you doing good burak"]

counts = map(count_words, documents)
#reduce accumulator, currval
def combine_counts_reducer(d1,d2):
  d = d1.copy() #copy the accumulator
  for word, count in d2.items(): #look innto the curr values 
    d[word] = d.get(word, 0) + count ## get the count of the accumulator and add the count of the currvalue items
  return d #accumulator processed
