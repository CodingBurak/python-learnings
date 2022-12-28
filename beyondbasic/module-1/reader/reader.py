import os

from reader.compressed import bzipped, gzipped

extension_map = {
  ".bz2": bzipped.opener,
  ".gz": gzipped.opener
}

class Reader:
  def __init__(self, filename) -> None:
    extension = os.path.splitext(filename)[1]
    opener = extension_map.get(extension, open)
    self.filename = filename
    self.file = opener(self.filename)
  
  def close(self):
    (self.file).close89
    
  def read(self):
    return self.file.read()