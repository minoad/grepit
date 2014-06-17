import urllib2

def get_links (html):
    import re
    pattern = r'<a href=["\'\s]*(\\*/{0,1}[A-Za-z0-9\./]+)\"'
    links = re.findall(re.compile (pattern), html)
    return(links)


html = (urllib2.urlopen ('https://github.com/minoad/grepit')).readlines ()
html = str (html)

print([n for n in get_links(html)])

#print(l)