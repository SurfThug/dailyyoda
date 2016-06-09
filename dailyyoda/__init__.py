import os
from datetime import date, timedelta
from dateutil.parser import parse

# convert the string into a date object
def parsedate(datestr):
  d = None

  if datestr == "today":
    d = date.today()
  elif datestr == "yesterday":
    d = date.today() - timedelta(days=1)
  elif datestr == "tomorrow":
    d = date.today() + timedelta(days=1)
  else:
    # try parsing it
    d = parse(datestr)
  return d

# return the day of year from a date object
def date2num(d):
  tt = d.timetuple()
  return tt.tm_yday

def read_db():
  this_dir, this_filename = os.path.split(__file__)
  dbpath = os.path.join(this_dir, "quotes.db")
  quotes = [line.rstrip('\n') for line in open(dbpath)]

# return the quote from a given index
def getquote(num):
  quotes = read_db()

  index = num % len(quotes)
  return quotes[index] 
