import sys
from urllib.request import urlopen


def getWords(url: str):
  """get words by url."""
  with urlopen(url) as story:
    story_words = []
    for line in story:
      line_words = line.decode("utf-8").split()
      for lineword in line_words:
        story_words.append(lineword)
  return story_words

def print_items(story_words):
  for word in story_words:
    print(word)

def main(url):
  print_items(getWords(url))

if __name__ == "__main__":
  main(sys.argv[1])


