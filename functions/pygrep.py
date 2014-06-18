
class Pygrep:

    def __init__(self, data):
        import urllib2,os.path
        from urlparse import urlparse
        self.path = data
        if os.path.isfile(data):
            with open(data) as content:
                contents=content.read()
        elif os.path.isdir(data):
            self.folderpath = data
            self.filelist = os.listdir(self.folderpath)
            contents=''
            for file in self.filelist:
                contents=contents+open(self.folderpath+file).read()
        elif (urlparse(data)).scheme != '':
            contents=(urllib2.urlopen(data)).readlines()
        else:
            contents=data
        self.contents=contents

    def apply(self, pattern):
        from re import findall, compile
        links=findall(compile(pattern),str(self.contents))
        ret=[]
        for i in links:
            n = [[self.path],[i]]
            ret.append(n)
        if len(ret) > 0 : return (ret)

    def getlinks(self):
         return(self.apply(r'<a href=["\'\s]*(\\*/{0,1}[A-Za-z0-9\./]+)\"'))
    def geturls(self):
        return(self.apply(r'https?://[\da-z\.-]+\.[a-z]+[/\d\w\.-]*'))
    def getips(self):
        return (self.apply(r'[0-2]?[0-9]?[0-9]{1}\.[0-2]?[0-9]?[0-9]{1}\.[0-2]?[0-9]?[0-9]{1}\.[0-2]?[0-9]?[0-9]{1}'))
    def getemails(self):
        return (self.apply(r'[a-zA-Z0-9_\.-]+@[\.a-zA-Z0-9_-]+\.[a-zA-Z\.]{2,6}'))
    def getpasswords(self):
        return(self.apply(r'[pP][aA][sS5][sS5][wW][oO0][rR3][dD][\W][a-zA-Z0-9_-]+'))
    def getimgur(self):
        return(self.apply(r'htt[p|ps]://[a-zA-Z0-9_-]*\.imgur+\.[a-zA-Z0-9_-]{2,3}/[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]{2,3}'))
    def getssn(self):
        return (self.apply(r'\W\d{3}[-\s:]?\d{2}[-\s:]?\d{4}\W'))
    def getcc_visa(self):
        return (self.apply(r'\W4[0-9]{3}[-\s:]?[0-9]{4}[-\s:]?[0-9]{4}\W'))
        #return (self.apply(r'4\d{3}\W?\d{4}\W?\d{4}'))
    def getcc_mastercard(self):
        return (self.apply(r'\W5[1-5]\d{2}[-\s:]?\d{4}[-\s:]?\d{4}\W'))
    def getcc_amex(self):
        return (self.apply(r'\W3\d{3}[-\s:]?\d{6}[-\s:]?\d{5}\W'))
    def getterms(self):
        return (self.apply(r'\W([lL][eE][aA][kK])|([hH][Aa][Cc][Kk])|([sS][tT][eE][aA][lL])|([vV][uU][lL][nN])\W'))


test = 'https://github.com/minoad/grepit'

import os
test = '/home/minoad/repos/sec_repo/python/pastebin/content/testfile.txt'


test = '/home/minoad/repos/sec_repo/python/pastebin/content/'




x=Pygrep(test)
r=[]
for i in os.listdir(test):
    n=Pygrep(test+i)
    nn=n.getcc_visa()
    if nn:
        r.append(nn)
for i in r: print(i)