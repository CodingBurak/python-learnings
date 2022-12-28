import unittest
import os

def analyze_text(filename):
  lines= 0
  chars = 0
  with open(filename) as f:
    for line in f:
      lines+=1
      chars = len(line)
    return lines, chars
      

class TextAnalysisTests(unittest.TestCase):
  
  def setUp(self) -> None:
    self.filename = "text_analysis_test_file.txt"
    with open(self.filename, "w") as f:
      f.write('''Now we are
              testing whether''')
      
  def tearDown(self) -> None:
    try:
      os.remove(self.filename)
    except:
      pass
  
  def test_func_runns(self):
    analyze_text(self.filename)
  
  def test_line_count(self):
    self.assertEqual(analyze_text(self.filename)[0], 2)
    
  def test_character_count(self):
    self.assertEqual(analyze_text(self.filename)[1], 29)
    
  def test_no_file(self):
    with self.assertRaises(IOError):
      analyze_text("noneexist")
      
  
    
if __name__ == "__main__":
  unittest.main()