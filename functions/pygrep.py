
class Pygrep:


    def __init__(self, data):
        import urllib2,os.path
        from urlparse import urlparse

        if os.path.exists(data):
            data=open(data)
        elif (urlparse(data)).scheme != '':
            data=(urllib2.urlopen(data)).readlines()



        print(data.__class__)
        self.data=data

    def apply(self, pattern):
        import re
        links=re.findall(re.compile(pattern),str(self.data))
        return (links)

    def getlinks(self):
         return(self.apply(r'<a href=["\'\s]*(\\*/{0,1}[A-Za-z0-9\./]+)\"'))






import urllib2

#Pygrep('<a href="/test.billy.com/yo">dfafdsda  <a href="/test.chris.com/yo">')

import os

Pygrep('https://github.com/minoad/grepit')

