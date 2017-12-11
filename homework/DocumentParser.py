# -*- coding: utf-8 -*-

import urllib2
import re

class DocumentParser(object):
    def remove_html(self, doc):
        return self.remove_all_tags(self.remove_css_js(doc))

    def remove_css_js(self, doc):
        return self.remove_tag_with_content(self.remove_tag_with_content(doc, "script"), "style")

    def remove_all_tags(self, doc):
        return re.sub('(?s)<[^<]+?>', '', doc)

    def remove_tag_with_content(self, doc, tag):
        return re.sub("(?s)<{}(.*?)>(.*?)<\/{}>".format(tag, tag), "", doc)

    def remove_punctuation(self, doc):
        punctuation_marks = [",", ".", ":", ";", "(", ")"]
        for mark in punctuation_marks:
            doc = doc.replace(mark, "")
        return doc

    def remove_stopwords(self, wordlist):
        with open("stopwords_pl", "r") as pl, open("stopwords_eng", "r") as eng:
            for stop_word in pl.read().splitlines():
                wordlist = filter(lambda w: w.lower() != stop_word, wordlist)
            for stop_word in eng.read().splitlines():
                wordlist = filter(lambda w: w.lower() != stop_word, wordlist)
        return wordlist

    def remove_incorrectly_parsed_words(self, wordlist):
        return filter(lambda w: (sum(1 for c in w[1:] if c.isupper())) < 1 or (sum(1 for c in w if c.isupper())) == len(w), wordlist)

    def get_wordlist(self, url):
        doc = urllib2.urlopen(url).read()
        return self.remove_incorrectly_parsed_words(self.remove_stopwords([word.strip() for word in self.remove_punctuation(self.remove_html(doc)).split(" ") if re.match("^[ąęłńóśżźa-zA-Z]+$", word)]))
