from computeNGD import computeNGD
import time
import numpy as np
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from parser import parser
import pickle

def save_obj(obj, name ):
    with open(name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


answers = [
["Bangladesh"],
# ["Short term fund"],
# ["Parliament"],
# ["President"],
# ["Pashupati"],
# ["Source of Hindu Philosophy"],
# ["Brahmaputra"],
# ["Kolkata"],
# ["Pyrometers"],
# ["crash"],
# ["Vishwa Bharti"],
# ["Himachal" ,"Pradesh"],
# ["radiation"],
# ["Deflation"],
# ["Ashok Chakra"],
# ["Nicobar Islands"],
# ["Leaching"],
# ["Convection"],
# ["Virus"],
# ["China"],
# ["Andhra" ,"Pradesh"],
# ["RBI"],
# ["Deficiencies of micronutrients and vitamins"],
# ["Supreme Court of India"],
]

questions = [
["India shares longest international boundary with which country"],
# ["Money market is a market for"],
# ["The Residuary powers of legislation under Indian Constitution rests with"],
# ["Appointments for all India Services are made by"],
# ["The people of the Indus valley civilisation worshipped"],
# ["The Upanishads are the"],
# ["Tsangpo is the other name in Tibet for"],
# ["The largest herbarium of India is located at"],
# ["Temperature of distant luminous bodies can be determined by"],
# ["In IT terminology failure in the kernel is called as"],
# ["Which of the following institutions was not founded by Mahatama Gandhi"],
# ["Which of the following State has become India's first carbon free State"],
# ["Energy travels from Sun to Earth through"],
# ["C.K. Naidu Cup is associated with which of the following sporting events"],
# ["Pump priming should be resorted to at a time of"],
# ["Which is the highest award for gallantry during peacetime"],
# ["At Barren Island, the only active volcano in India is situated in"],
# ["The transfer of minerals from top soil to subsoil through soil-water is called"],
# ["Heat is transmitted from higher temperature to lower temperature through the actual motion of the molecules in"],
# ["Polio is caused by"],
# ["Which country is in the process of building the largest single Aperture Radio Telescope - FAST"],
# ["The Kovvada Nuclear Park project is proposed to be setup in which State"],
# ["Fixed Foreign Exchange Rate can be changed by"],
# ["In bio fortification technique plant breeders use breeding to overcome"],
# ["Which Institution has the final authority to interpret the Constitution of India"],
]


options_all = [
[["Bangladesh"], ["China"], ["Nepal"], ["Bhutan"]],
# [["Short term fund"], ["Long term" ,"fund"], ["Negotiable instruments"], ["Sale of shares"]],
# [["President"],["Prime Minister"],["Parliament"],["States"]],
# [["UPSC"],["President"],["Prime Minister"],["Parliament"]],
# [["Vishnu"],["Pashupati"],["Indra"],["Brahma"]],
# [["Great Epics"],["Story Books"],["Source of Hindu Philosophy"],["Law Books"]],
# [["Kosi"],["Gandak"],["Brahmaputra"],["Ganga"]],
# [["Kolkata"],["Lucknow"],["Mumbai"],["Coimbatore"]],
# [["Mercury thermometers"],["Gas thermometers"],["Pyrometers"],["Colour thermometers"]],
# [["crash"],["crash dump"],"dump",["Kernel error"]],
# [["Sabarmati Ashram"],["Sevagram Ashram"],["Vishwa Bharti"],["Phoenix Ashram"]],
# [["Himachal Pradesh"],["Madhya Pradesh"],["Uttar Pradesh"],["Maharashtra"]],
# [["conduction"],["convection"],["radiation"],["modulation"]],
# [["Tennis"],["Cricket"],["Hockey"],["Golf"]],
# [["Inflation"],["Deflation"],["Stagflation"],["Reflation"]],
# [["Vir Chakra"],["Param Vir Chakra"],["Ashok Chakra"],["Mahavir Chakra"]],
# [["Andaman Islands"],["Nicobar Islands"],["Lakshadweep"],["Minicoy"]],
# [["Percolation"],["Conduction"],["Leaching"],["Transpiration"]],
# [["Conduction"],["Convection"],["Radiation"],["Both conduction and convection"]],
# [["Bacteria"],["Virus"],["Fungus"],["Protozoa"]],
# [["Japan"],["China"],["USA"],["Russia"]],
# [["Rajasthan"],["Uttar" ,"Pradesh"],["Andhra Pradesh"],["Karnataka"]],
# [["RBI"],["SEBI"],["Ministry" ,"of" ,"Finance"],["FIPB"]],
# [["Loss due to insect pests"],["Decrease in food production"],["Deficiencies of micronutrients and vitamins"],["Loss due to plant diseases"]],
# [["Parliament"],["Supreme Court of India"],["President"],["Attorney General of India"]]
]

ps = PorterStemmer()
lmtzr = WordNetLemmatizer()

# ---------------------------------------------------------------------

words = []
word_id = {}
ids = 0
for question in questions:
	question = parser(question[0], ps, lmtzr)
	for word in question:
		if word not in words:
			words.append(word)
			word_id[word] = ids
			ids+=1
for options in options_all:
	for option in options:
		option = parser(option[0], ps, lmtzr)
		for word in option:
			if word not in words:
				words.append(word)
				word_id[word] = ids
				ids+=1

print("web scraping started")
rw = 0
print("We have " + str(len(words)) + " words")
wwMat = np.zeros((len(words),len(words)))

for word in words:
	time_row = time.time()
	rw+=1
	for w2 in words:
		time_el = time.time()
		print("working towards ({0},{1}) ".format(word,w2))
		wwMat[word_id[word],word_id[w2]] = computeNGD(word,w2)
		print("Time to find an element of row " + str(rw) + " is " + str(time.time()-time_el))
	wwMat[word_id[word],:] = wwMat[word_id[word],:]#/wwMat[word_id[word],word_id[word]] 
	#rw+=1
	print("Time to reach row " + str(rw) + " is "+ str(time.time()-time_row))
mx = np.max(wwMat)
wwMat = 1 - wwMat/mx
np.save('wwMat', wwMat)
save_obj(word_id, "word_ids")
