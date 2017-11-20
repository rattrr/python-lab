import urllib2

def save_html_to_file(url):
    with open("site.html", 'w') as sitefile:
        sitefile.write(urllib2.urlopen(url).read())

save_html_to_file('http://hasthelargehadroncolliderdestroyedtheworldyet.com/');
