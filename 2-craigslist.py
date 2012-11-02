#!/usr/bin/env python
import mechanize
def main():
    b = mechanize.Browser()
    b.set_handle_robots(False)
    b.open('http://dallas.craigslist.org/dal/web/') 
    pg = b.open('http://dallas.craigslist.org').read()
    return pg
if __name__ == '__main__':
    import sys
    sys.stdout.write(main())