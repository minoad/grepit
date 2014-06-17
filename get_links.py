__author__ = 'minoad'
import urllib2
#this simply gets all of the html links from a string

def get_links(html):
    import re
    html = str(html)
    lnks=re.search('<a href=\"/[A-Za-z0-9]+\"',html)
    print(lnks.group(0))

'''
    for n in last:
        url=re.search('<a href=\"/([A-Za-z0-9]{8,8})\"',n)
        new_url='http://pastebin.com/'+url.group(1)
'''

'''
        try:
            w=urllib2.urlopen(new_url)
            uniq_f=uuid.uuid4()
            nu=(n.replace('<a href=\"/','')).replace('"','')
            content=str(w.read())
            c_sea=re.search('<textarea id=\"paste_code\" class=\"paste_code\" name=\"paste_code\" onkeydown=\"return catchTab\(this,event\)\">(.*)</textarea>',content)
            file=open('content/'+filename_gen(nu)+'.txt','w')
            file.write(c_sea.group(1))
            file.close()
        except:
            pass
'''

inp = urllib2.urlopen('http://stackoverflow.com/questions/7696924/multiline-comments-in-python')
res=inp.readlines()



print(str(res))