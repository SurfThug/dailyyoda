import os
from datetime import date, timedelta
from dateutil.parser import parse

class dailyyoda:

  def __init__(self, dbname):
    filename = None
    if dbname == 'test':
      filename = 'test.db'
    elif dbname == 'yoda':
      filename = 'quotes.db'
    else:
      raise ValueError("Unknown dbname: " + dbname + ".  Acceptable options: test, yoda")

    self.db = self.load_db(filename)

  # convert the string into a date object
  def parse_date(self, datestr):
    d = None

    if datestr == "today":
      d = date.today()
    elif datestr == "yesterday":
      d = date.today() - timedelta(days=1)
    elif datestr == "tomorrow":
      d = date.today() + timedelta(days=1)
    else:
      # try parsing it
      d = parse(datestr).date()
    return d

  # return the day of year from a date object
  def date2num(self, d):
    tt = d.timetuple()
    return tt.tm_yday

  # load the quote db from file
  def load_db(self, filename):
    this_dir, this_filename = os.path.split(__file__)
    dbpath = os.path.join(this_dir, filename)
    db = [line.rstrip('\n') for line in open(dbpath)]
    return db

  # return the quote from a given index
  def lookup_quote(self, num):
    index = num % len(self.db)
    return self.db[index] 

  # return the quote from a given date
  def get_quote(self, datestr):
    d = self.parse_date(datestr)
    num = self.date2num(d)
    quote = self.lookup_quote(num)
    return quote
