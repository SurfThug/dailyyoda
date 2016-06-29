import unittest
import dailyyoda
from datetime import date, timedelta

class dailyyoda_tests(unittest.TestCase):
  
  def setUp(self):
    self.dy = dailyyoda.dailyyoda("test")

  def test_parse_date(self):
    # today
    date1 = date.today()
    date2 = self.dy.parse_date('today')
    self.assertIsNotNone(date2)
    self.assertEquals(date1, date2)

    # yesterday
    date1 = date.today() - timedelta(days=1)
    date2 = self.dy.parse_date('yesterday')
    self.assertIsNotNone(date2)
    self.assertEquals(date1, date2)

    # tomorrow
    date1 = date.today() + timedelta(days=1)
    date2 = self.dy.parse_date('tomorrow')
    self.assertIsNotNone(date2)
    self.assertEquals(date1, date2)

    # error cases
    with self.assertRaises(ValueError):
      self.dy.parse_date('last friday')
    with self.assertRaises(ValueError):
      self.dy.parse_date('TODAY')

    # specific dates
    date1 = date(1977, 5, 25)
    date2 = self.dy.parse_date('1977-05-25')
    self.assertIsNotNone(date2)
    self.assertEquals(date1, date2)

    date2 = self.dy.parse_date('1977-5-25')
    self.assertEquals(date1, date2)

    date2 = self.dy.parse_date('5/25/1977')
    self.assertEquals(date1, date2)

    date2 = self.dy.parse_date('May 25, 1977')
    self.assertEquals(date1, date2)

  def test_date2num(self):
    # first day of year
    date1 = date(1900, 1, 1)
    num1 = 1
    num2 = self.dy.date2num(date1)
    self.assertEquals(num1, num2)

    date1 = date(1901, 1, 1)
    num1 = 1
    num2 = self.dy.date2num(date1)
    self.assertEquals(num1, num2)

    # second day of year
    date1 = date(1900, 1, 2)
    num1 = 2
    num2 = self.dy.date2num(date1)
    self.assertEquals(num1, num2)

    # last day of year
    date1 = date(1999, 12, 31)
    num1 = 365
    num2 = self.dy.date2num(date1)
    self.assertEquals(num1, num2)

    date1 = date(2000, 12, 31)
    num1 = 366
    num2 = self.dy.date2num(date1)
    self.assertEquals(num1, num2)

    # no leap year in 1900?
    date1 = date(1900, 12, 31)
    num1 = 365
    num2 = self.dy.date2num(date1)
    self.assertEquals(num1, num2)

    # invalid argument
    with self.assertRaises(AttributeError):
      self.dy.date2num("1900-01-01")

  def test_load_db(self):
    # test db
    db = self.dy.load_db("test.db")
    self.assertEquals(len(db), 4)
    self.assertEquals(db[0], "sample quote 1")
    self.assertEquals(db[1], "sample quote 2")
    self.assertEquals(db[2], "sample quote 3")
    self.assertEquals(db[3], "sample quote 4")

    # quotes database (may be empty)
    db = self.dy.load_db("quotes.db")
    self.assertIsNotNone(db)

    # non-existant file
    with self.assertRaises(IOError):
      self.dy.load_db("invalid.db")

  def test_lookup_quote(self):
    self.assertEquals(self.dy.lookup_quote(0), "sample quote 1")
    self.assertEquals(self.dy.lookup_quote(1), "sample quote 2")
    self.assertEquals(self.dy.lookup_quote(2), "sample quote 3")
    self.assertEquals(self.dy.lookup_quote(3), "sample quote 4")
    self.assertEquals(self.dy.lookup_quote(4), "sample quote 1")
    self.assertEquals(self.dy.lookup_quote(5), "sample quote 2")
    self.assertEquals(self.dy.lookup_quote(-1), "sample quote 4")

    # invalid argument
    with self.assertRaises(TypeError):
      self.dy.lookup_quote("1")

  def test_get_quote(self):
    # check specific dates
    self.assertEquals(self.dy.get_quote("1900-01-01"), "sample quote 2")
    self.assertEquals(self.dy.get_quote("1900-01-02"), "sample quote 3")
    self.assertEquals(self.dy.get_quote("1977-05-25"), "sample quote 2")
   
    # invalid argument
    with self.assertRaises(AttributeError):
      self.dy.get_quote(1)

  def test___init__(self):
    dy2 = dailyyoda.dailyyoda('test')
    self.assertEquals(dy2.lookup_quote(0), "sample quote 1")
    
    dy2 = dailyyoda.dailyyoda('yoda')

    # invalid db option
    with self.assertRaises(ValueError):
      dailyyoda.dailyyoda('invalid')


if __name__ == '__main__':
  unittest.main()
