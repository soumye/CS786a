import urllib
def queryWikiNumPages(query):

	qstring = 'https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch='+ query + '&srprop=timestamp&format=json&maxlag=5'
	s = urllib.urlopen(qstring).read()
	i = s.find('hits')+6
	while (s[i] != '}' and s[i] != ','):
		i += 1
	out = s[s.find('hits')+6:i]
	return float(out);
