import urllib
import urllib2
import sys
import os
import time

thing = 'http://ctfstore.mit.edu/Team_'
aktie = '/aktie.apk'
andymail = '/andymail.apk'
appstore = '/appstore.apk'
ctfbank = '/ctfbank.apk'
ctfmicro = '/ctfmicro.apk'
passwords = '/passwords.apk'
ssn = '/snn.apk'
team = '/team'
cygwin = "C:\cygwin64\home\\"
time = str(time.time())

for x in range(1, 39):
    try:
        url = thing + str(x) + aktie
        url1 = thing + str(x) + andymail
        url2 = thing + str(x) + appstore
        url3 = thing + str(x) + ctfbank
        url4 = thing + str(x) + ctfmicro
        url5 = thing + str(x) + passwords
        url6 = thing + str(x) + andymail
        newpath = cygwin + time + team + str(x)
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        urllib.urlretrieve(url, time + team + str(x) + aktie)
        urllib.urlretrieve(url1, time + team + str(x) + andymail)
        urllib.urlretrieve(url2, time + team + str(x) + appstore)
        urllib.urlretrieve(url3, time + team + str(x) + ctfbank)
        urllib.urlretrieve(url4, time + team + str(x) + ctfmicro)
        urllib.urlretrieve(url5, time + team + str(x) + passwords)
        urllib.urlretrieve(url6, time + team + str(x) + ssn)
    except:
        print sys.exc_info()[0], x
        continue
    
