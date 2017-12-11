# -*- coding: utf-8 -*-

import urllib2
import sys

class WikipediaLinksGenerator(object):
    def __init__(self, n, pagesfile):
        self.links = list()
        self.fill_links(n)
        self.writeToFile(pagesfile)

    def fill_links(self, n):
        for i in xrange(n):
            self.links.append(self.generate())
            print "[{}] {}".format(str(i), self.links[i])

    def generate(self):
        response = urllib2.urlopen('https://en.wikipedia.org/wiki/Special:Random')
        while(response.geturl() in self.links):
            response = urllib2.urlopen('https://en.wikipedia.org/wiki/Special:Random')
        return response.geturl()

    def writeToFile(self, pagesfile):
        with open(pagesfile, "w") as pagesfile:
            pagesfile.write("\n".join(self.links))

if __name__ == "__main__":
    try:
        wlg = WikipediaLinksGenerator(int(sys.argv[1]), sys.argv[2])
    except (IndexError, ValueError):
        print "Input error\nUsage: python WikipediaLinksGenerator.py number_of_links filename"
