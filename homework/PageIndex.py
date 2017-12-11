# -*- coding: utf-8 -*-

import cPickle
import os.path
from DocumentParser import DocumentParser

class PageIndex(object):
    def __init__(self, indexfile="index.pickle", pagesfile="pages"):
        if not os.path.isfile(indexfile):
            print "No index file found"
            self.pagesdict = dict()
            with open(pagesfile, "r") as pages:
                self.pageslist = pages.read().splitlines()
            print "Making new one: "
            self.find_most_common_words()
            if(indexfile.endswith(".pickle")):
                self.dump_index(indexfile)
                print "Index file saved in {}\n".format(indexfile)
        else:
            self.load_index(indexfile)
            print "Loaded index file"

    def __str__(self):
        to_print = ""
        for page, words in self.pagesdict.iteritems():
            to_print += "     {}:\n{}\n\n".format(page, "\n".join("|{}| {}".format(str(e[0]), e[1]) for e in words))
        return to_print

    def dump_index(self, indexfile):
        with open(indexfile, 'wb') as index:
            cPickle.dump(self.__dict__, index)

    def load_index(self, indexfile):
        with open(indexfile, 'rb') as index:
            tmp = cPickle.load(index)
            self.__dict__.update(tmp)

    def find_most_common_words(self):
        dp = DocumentParser()
        for index, page in zip(xrange(len(self.pageslist)), self.pageslist):
            wordlist = dp.get_wordlist(page)
            print "  [{}/{}] {}".format(index, len(self.pageslist), page)
            occurrences = dict((word, wordlist.count(word)) for word in wordlist)
            self.pagesdict[page] = [(occurrences[k], k) for k in sorted(occurrences, key = occurrences.get, reverse = True)[:5]]
