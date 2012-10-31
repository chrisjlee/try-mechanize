#!/usr/bin/env python
import mechanize

b = mechanize.Browser()
b.set_handle_robots(False)
pg = b.open('http://www.google.com').read()
print pg