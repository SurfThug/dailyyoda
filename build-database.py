#!/usr/bin/python

import subprocess as sub
import re

# Got a 503 response when using urllib2
#import urllib2
#url = 'http://morecoolquotes.com/famous-yoda-quotes/'
#response = urllib2.urlopen(url)
#content = response.read()
#print content

# curl the page with the quotes
curl = sub.Popen(['curl', 'http://morecoolquotes.com/famous-yoda-quotes/'],stdout=sub.PIPE,stderr=sub.PIPE)
content, errors = curl.communicate()

#print content
#content = "<li>one &#8211; Yoda</li><li>two &#8211; Yoda</li>"

# extract the quotes
quotes = re.findall('<li>([^<]+) &#8211; Yoda</li>', content)

# write the contents to a file
f = open('quotes.db', 'w')
for quote in quotes:
  f.write(quote + "\n")
f.close()
