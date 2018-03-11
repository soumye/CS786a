import urllib.request
import time
import math

def queryGoogleNumPages(query):
	offset = 23;
	qstring = 'https://www.google.co.in/search?source=hp&ei=-ZWFWrPvGY20vwTv9ZGgAQ&q=' + query

	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
	req = urllib.request.Request(qstring, headers = headers)
	page = urllib.request.urlopen(req)
	s = page.read().decode('utf-8')
	sIdx = s.find('id="resultStats"');
	# print(s[sIdx:])
	eIdx = s[sIdx:].find(' results');
	# eIdx = eIdx[1];

	rstring = s[sIdx+offset:sIdx+eIdx-1];
	rstring = rstring.replace(',','')
	out = math.log(float(rstring));

	time.sleep(2)           # very important if you don't want to seem like a bot and have your IP blocked by Google
	return float(rstring)

# print(queryGoogleNumPages("hello"))