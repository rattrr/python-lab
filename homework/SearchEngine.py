# -*- coding: utf-8 -*-

from PageIndex import PageIndex

class SearchEngine(object):
    def __init__(self, pageindex):
        self.pageindex = pageindex

    def search(self, word):
        print "\nLooking for word '{}'".format(word)
        results = self.find_exact_word(word)
        if len(results) < 3:
            search_more = raw_input("\nFound less than 3 results. Search for similar words?  [Y\N]: ")
            if search_more.upper() == "Y":
                self.search_more_words(word, results)
            elif search_more.upper() == "N":
                print "OK, searching ended"
            else:
                print "Incorrect input"


    def find_exact_word(self, word):
        results = list()
        for page, words in self.pageindex.pagesdict.iteritems():
            if word.lower() in [w[1].lower() for w in words]:
                results.append(page)
                print " Found '{}' in: {}".format(word, page)
        return results

    def search_more_words(self, word, results):
        to_slice = 0
        while(len(word)-to_slice > 2*len(word)/3):
            print "\nLooking for words starting with: {}".format(word[:len(word)-to_slice])
            if not self.find_similar_words(word[:len(word)-to_slice], results):
                print "  Found nothing more"
            to_slice += 1

    def find_similar_words(self, sliced, results):
        found_flag = False
        for page, words in self.pageindex.pagesdict.iteritems():
            for word in [w[1] for w in words]:
                if word.lower().startswith(sliced.lower()) and page not in results:
                    found_flag = True
                    results.append(page)
                    print "  Found '{}' in: {}".format(word, page)
        return found_flag

if __name__ == "__main__":
    try:
        pi = PageIndex()
        se = SearchEngine(pi)
        #print pi # to view index of pages with 5 most common words
        input_word = raw_input("\n\nType word to search for (or type \033[1mq\033[0m to exit): ")
        while(input_word != 'q'):
            se.search(input_word)
            input_word = raw_input("\n\nType word to search for (or type \033[1mq\033[0m to exit): ")
    except KeyboardInterrupt:
        print " Received keyboard interrupt"
