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


'''
test = 'https://github.com/minoad/grepit'

import os
test = '/home/minoad/repos/sec_repo/python/pastebin/content/testfile.txt'


test = '/home/minoad/repos/sec_repo/python/pastebin/content/'

#test='http://www.neohapsis.com'

#test = 'not a file or url.10.9.105.43 password=testing 3794 746376-91117 224 42 5523 229-52-8064 5178-9924-2064-5514 password 4876212433560846 testing password:testcolon test@neo.neohapsis.com 4356 4391 4097 4453 https://mail.neohapsis.com I am simply a string. minoad@gmail.com mnorman@neohapsis.com micah.norman@neohapsis.com 4356-4391-4097-4453 dayshttp://b.hatena.ne.jp/entry/community.ec21.com/forum/viewtopic.jsp?topic_id=129793https://charahub.com/character/296954/Bianca-C.-Cav'
x=Pygrep(test)
#print(Pygrep(test).getlinks())
r=[]
for i in os.listdir(test):
    n=Pygrep(test+i)
    nn=n.getimgur()
    if nn:
        r.append(nn)
#print(x.geturls())
for i in r: print(i)
#print(r)

''