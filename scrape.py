import urllib2
import datetime
from bs4 import BeautifulSoup
import time
import socket

def stripNonASCII(text):
    return ''.join([i if ord(i) < 128 else '' for i in text])

def scrape(path, filter, sites):
    results = {}
    for s in sites:
        print(s + " scrape has begun..." + '\r')
	
        try:
            soup = BeautifulSoup(urllib2.urlopen(s + path).read())
        except:
            print(FAIL + s + ' has timed out!' + ENDC)
            continue

        posts = soup.select('.pl')
        urls = []
        
        for post in posts:
            if str(datetime.datetime.now().day) in post.select('time')[0]['datetime'] or str(datetime.datetime.now().day-1) in post.select('time')[0]['datetime']:
                urls.append(post.select('a')[0])

        for url in urls:
            if('craigslist' not in url.get('href') and (filter in url.string.lower())):
                results[url.string] = s + url.get('href')
        
        print(s + " has been scraped. Waiting to start next URL..." + '\r')

        time.sleep(2)

    print('Total Results for ' + filter + ': ' + str(len(results)))

    return results

timeout = 5
socket.setdefaulttimeout(timeout)

sites = ['http://boston.craigslist.org',
'http://capecod.craigslist.org',
'http://southcoast.craigslist.org',
'http://worcester.craigslist.org',
'http://westernmass.craigslist.org',
'http://nh.craigslist.org',
'http://burlington.craigslist.org',
'http://maine.craigslist.org',
'http://newlondon.craigslist.org',
'http://hartford.craigslist.org',
'http://newhaven.craigslist.org',
'http://nwct.craigslist.org',
'http://providence.craigslist.org']

FAIL = '\033[91m'
ENDC = '\033[0m'

searches = [
    {'url': '/search/cta?query=rs&srchType=T&minAsk=&maxAsk=6000&hasPic=1&autoMinYear=1999&autoMaxYear=2001&autoMakeModel=', 'item': 'subaru'},
    {'url': '/search/cta?query=miata&srchType=T&hasPic=1&maxAsk=5000&autoMaxYear=1997', 'item': 'miata'}
    ]

fl = open('./results.html', 'w+')
fl.write('<html><body>')
results = {}

for search in searches:
    results.update(scrape(search['url'], search['item'], sites))


for k, v in results.iteritems():
        fl.write('<a target="_blank" href="' + v + '">' + stripNonASCII(k) + '</a>' + '<br>')

fl.write('</body></html>')
fl.close()
