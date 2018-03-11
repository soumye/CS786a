import math
from queryWikiNumPages import queryWikiNumPages
from queryGoogleNumPages import queryGoogleNumPages

def computeNGD(a,b):
	# la = queryWikiNumPages(a);
	# lb = queryWikiNumPages(b);
	# lab = queryWikiNumPages(a + '+' + b);

	lN = math.log(47000000000);         #number of webpages indexed by Google in Feb 2018
	la = queryGoogleNumPages(a);
	lb = queryGoogleNumPages(b);
	lab = queryGoogleNumPages(a + '+' + b);

	# print(la, lb, lab, lN)
	NGD = (math.log(max(la,lb)) - math.log(lab))/(lN - math.log(min(la,lb)));
	return NGD

# print(computeNGD("gauss","math"))