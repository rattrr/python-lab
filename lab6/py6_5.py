from xml.dom import minidom
import urllib2

def save_xml_to_file(url):
    with open("site.xml", 'w') as sitefile:
        sitefile.write(urllib2.urlopen(url).read())


save_xml_to_file('http://feeds.feedburner.com/niebezpiecznik?format=xml')
xmldoc = minidom.parse('site.xml')
titlelist = xmldoc.getElementsByTagName('title')[1:]
publishedlist = xmldoc.getElementsByTagName('published')
authorlist = xmldoc.getElementsByTagName('author')

for title, published, author in zip(titlelist, publishedlist, authorlist):
    print "title: " + title.childNodes[0].nodeValue
    print "author: " + author.getElementsByTagName('name')[0].childNodes[0].nodeValue
    print "published: " + published.childNodes[0].nodeValue
    print '\n'
