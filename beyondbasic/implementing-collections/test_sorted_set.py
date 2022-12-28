import unittest

from sorted_set import SortedSet
from collections.abc import(Container, Sized, Sequence, Iterable)

class TestConstruction(unittest.TestCase):
  
  def test_empty(self):
    s = SortedSet([])
    
  def test_from_sequence(self):
    s = SortedSet([7,8,3,1])
  
  def test_with_duplicates(self):
    s = SortedSet([1,1,2])
    
  def test_from_iterable(self):
    def gen1234():
      yield 1
      yield 2
      yield 3
      yield 4
    
    g = gen1234()
    s = SortedSet(g)
    
  def test_from_no_param(self):
    s = SortedSet()
    

class TestContainerProtocol(unittest.TestCase):
  
  def setUp(self):
    self.s = SortedSet([1,3,5,4])

  def test_positive_contained(self):
    self.assertTrue(1 in self.s)
    
  def test_negative_contained(self):
    self.assertFalse(0 in self.s)
    
  def test_pos_contained_not(self):
    self.assertTrue(0 not in self.s)
  
  def test_neg_contained_not(self):
    self.assertFalse(3 not in self.s)
    
  def test_contatiner(self):
    self.assertTrue(issubclass(SortedSet, Container))
    
    
class TestSizedProtocol(unittest.TestCase):
  
  def test_empty(self):
    s = SortedSet()
    self.assertEqual(len(s), 0)
    
  def test_one(self):
    s = SortedSet([1])
    self.assertEqual(len(s), 1)
  
  def test_10(self):
    s = SortedSet(range(10))
    self.assertEqual(len(s), 10)
    
  def test_with_dupl(self):
    s = SortedSet([1,1,1,1])
    self.assertTrue(len(s),1)
    
  def test_contatiner(self):
    self.assertTrue(issubclass(SortedSet, Sized))

class TestIterable(unittest.TestCase):
  
  def setUp(self) -> None:
    self.s = SortedSet([7,2,2,1])
    
  def test_iterable(self):
    i = iter(self.s)
    self.assertTrue(next(i),7)
    self.assertTrue(next(i),2)
    self.assertTrue(next(i),1)
    self.assertRaises(StopIteration, lambda: next(i))
    
  def test_for_loop(self):
    index = 0
    expected = [1,2,7]
    
    for item in self.s:
      self.assertEqual(item, expected[index])
      index +=1
      
  def test_contatiner(self):
    self.assertTrue(issubclass(SortedSet, Iterable))
    
class TestSequence(unittest.TestCase):
  
  def setUp(self) -> None:
    self.s = SortedSet([1,2,3,4,5])
    
  def test_index_zero(self):
    self.assertTrue(self.s[0], 1)
    
  def test_index_4(self):
    self.assertTrue(self.s[4], 5)
    
  def test_outbound(self):
    self.assertRaises(IndexError, lambda: self.s[10])
    
  def test_minus_one(self):
    self.assertTrue(self.s[-1], 5)
    
  def test_minus_five(self):
    self.assertTrue(self.s[-5], 1)
    
  def test_neg_outbound(self):
    with self.assertRaises(IndexError):
      self.s[-6]
    self.assertRaises(IndexError, lambda: self.s[-6])
    
  def test_slice_from_start(self):
    self.assertEqual(self.s[:3], SortedSet([1,2,3]))
    
  def test_slice_from_end(self):
    self.assertEqual(self.s[3:], SortedSet([4,5]))
    
  def test_slice_empty(self):
    self.assertEqual(self.s[10:], SortedSet())
    
  def test_slice_arbitrary(self):
    self.assertEqual(self.s[2:4], SortedSet([3,4]))
    
  def test_slice_full(self):
    self.assertEqual(self.s[:], self.s)
    
  def test_reversed(self):
    s = SortedSet([1,2,3,4])
    r = reversed(s)
    
    self.assertEqual(next(r), 4)
    self.assertEqual(next(r), 3)
    self.assertEqual(next(r), 2)
    self.assertEqual(next(r), 1)
    
    with self.assertRaises(StopIteration):
      next(r)
      
  def test_index_positive(self):
    s = SortedSet([1,5,3])
    self.assertTrue(s.index(5), 1)
    
  def test_index_negative(self):
    s = SortedSet([1,2,4])
    with self.assertRaises(ValueError):
      s.index(5)
  
  def test_count_positive(self):
    s = SortedSet([1,5,3])
    self.assertEqual(s.count(1), 1)
    
  def test_count_positive_non_existing(self):
    s = SortedSet([1,5,3])
    self.assertEqual(s.count(123), 0)
    
  def test_contatiner(self):
    self.assertTrue(issubclass(SortedSet, Sequence))
    
    
  def test_plus(self):
    s = SortedSet([1,2,3])
    t = SortedSet([4,5,6])
    self.assertEqual(s + t, SortedSet([1,2,3,4,5,6]))
    
  def test_same_plus(self):
    s = SortedSet([1,2,3])
    t = SortedSet([1,2,3])
    self.assertEqual(s+t, SortedSet([1,2,3]))
    
    
  def test_plus_some(self):
    s = SortedSet([1,2,3])
    t = SortedSet([3,5,6])
    self.assertEqual(s+t, SortedSet([1,2,3,5,6]))
    
  def test_mul(self):
    s = SortedSet([1,2,3])
    self.assertEqual(s * 0, SortedSet())
    
  def test_mul_umb(self):
    s = SortedSet([1,2,3])
    self.assertEqual(s * 100, s)
    
  def test_mul_r(self):
    s = SortedSet([1,2,3])
    self.assertEqual( 0 * s, SortedSet())
    
  def test_mul_umb_r(self):
    s = SortedSet([1,2,3])
    self.assertEqual( 100 * s, s)
    
    
  def test_mutable(self):
    s = SortedSet([1,2,3])
    s.add(5)
    self.assertEqual( SortedSet([1,2,3,5]), s)
    
  def test_discard_mutable(self):
    s = SortedSet([1,2,3])
    s.discard(2)
    self.assertEqual(SortedSet([1,3]), s)
  
      
    
class TestRepr(unittest.TestCase):
  
  def test_repr_empty(self):
    s = SortedSet()
    self.assertEqual(repr(s), "SortedSet()")
  
  def test_repr_some(self):
    s = SortedSet([1,4,2])
    self.assertEqual(repr(s), "SortedSet([1, 2, 4])")
    
class TestEquality(unittest.TestCase):
  def test_equal_pos(self):
    s = SortedSet([1,4,2])
    s2 = SortedSet([1,4,2])
    self.assertTrue(s == s2)
  def test_equal_neg(self):
    s = SortedSet([1,4,2])
    s2 = SortedSet([1,42,4])
    self.assertFalse(s == s2)
    
  def test_equal_mismatch(self):
    s = SortedSet([1,4,2])
    s2 = [1,4,2]
    self.assertFalse(s == s2)
    
  def test_self(self):
    s = SortedSet([1,2,3])
    self.assertTrue(s == s)
    
    
class TestInEquality(unittest.TestCase):
  def test_equal_pos(self):
    s = SortedSet([1,4,2])
    s2 = SortedSet([2,5,3])
    self.assertTrue(s != s2)
  def test_equal_neg(self):
    s = SortedSet([1,4,2])
    s2 = SortedSet([1,2,4])
    self.assertFalse(s != s2)
    
  def test_equal_mismatch(self):
    s = SortedSet([1,4,2])
    s2 = [1,4,2]
    self.assertTrue(s != s2)
    
  def test_self(self):
    s = SortedSet([1,2,3])
    self.assertFalse(s != s)
    

  
  
if __name__ == "__main__":
  unittest.main()