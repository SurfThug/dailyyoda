import unittest
import dailyyoda

class dailyyoda_tests(unittest.TestCase):
  
  def setUp(self):
    self.dy = dailyyoda.dailyyoda("test")

  def test_date2num(self):
    date = self.dy.parse_date('today')
    self.assertIsNotNone(date)

if __name__ == '__main__':
  unittest.main()
