from predict import predict
import numpy as np
import numpy as np
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from parser import parser
#Attention based model
# Question = ["India", "shares", "longest", "international", "boundary", "with", "which", "country"]
# Question = ["India", "longest", "boundary"]

# Options = [["Bangladesh"], ["China"]]

answers = [
["Bangladesh"],
["Short term fund"],
["Parliament"],
["President"],
["Pashupati"],
["Source of Hindu Philosophy"],
["Brahmaputra"],
["Kolkata"],
["Pyrometers"],
["crash"],
["Vishwa Bharti"],
["Himachal" ,"Pradesh"],
["radiation"],
["Cricket"],
["Deflation"],
["Ashok Chakra"],
["Nicobar Islands"],
["Leaching"],
["Convection"],
["Virus"],
["China"],
["Andhra" ,"Pradesh"],
["RBI"],
["Deficiencies of micronutrients and vitamins"],
["Supreme Court of India"],
]

questions = [
["India shares longest international boundary with which country"],
["Money market is a market for"],
["The Residuary powers of legislation under Indian Constitution rests with"],
["Appointments for all India Services are made by"],
["The people of the Indus valley civilisation worshipped"],
["The Upanishads are the"],
["Tsangpo is the other name in Tibet for"],
["The largest herbarium of India is located at"],
["Temperature of distant luminous bodies can be determined by"],
["In IT terminology failure in the kernel is called as"],
["Which of the following institutions was not founded by Mahatama Gandhi"],
["Which of the following State has become India's first carbon free State"],
["Energy travels from Sun to Earth through"],
["C.K. Naidu Cup is associated with which of the following sporting events"],
["Pump priming should be resorted to at a time of"],
["Which is the highest award for gallantry during peacetime"],
["At Barren Island, the only active volcano in India is situated in"],
["The transfer of minerals from top soil to subsoil through soil-water is called"],
["Heat is transmitted from higher temperature to lower temperature through the actual motion of the molecules in"],
["Polio is caused by"],
["Which country is in the process of building the largest single Aperture Radio Telescope - FAST"],
["The Kovvada Nuclear Park project is proposed to be setup in which State"],
["Fixed Foreign Exchange Rate can be changed by"],
["In bio fortification technique plant breeders use breeding to overcome"],
["Which Institution has the final authority to interpret the Constitution of India"],
]


options_all = [
[["Bangladesh"], ["China"], ["Nepal"], ["Bhutan"]],
[["Short term fund"], ["Long term" ,"fund"], ["Negotiable instruments"], ["Sale of shares"]],
[["President"],["Prime Minister"],["Parliament"],["States"]],
[["UPSC"],["President"],["Prime Minister"],["Parliament"]],
[["Vishnu"],["Pashupati"],["Indra"],["Brahma"]],
[["Great Epics"],["Story Books"],["Source of Hindu Philosophy"],["Law Books"]],
[["Kosi"],["Gandak"],["Brahmaputra"],["Ganga"]],
[["Kolkata"],["Lucknow"],["Mumbai"],["Coimbatore"]],
[["Mercury thermometers"],["Gas thermometers"],["Pyrometers"],["Colour thermometers"]],
[["crash"],["crash dump"],"dump",["Kernel error"]],
[["Sabarmati Ashram"],["Sevagram Ashram"],["Vishwa Bharti"],["Phoenix Ashram"]],
[["Himachal Pradesh"],["Madhya Pradesh"],["Uttar Pradesh"],["Maharashtra"]],
[["conduction"],["convection"],["radiation"],["modulation"]],
[["Tennis"],["Cricket"],["Hockey"],["Golf"]],
[["Inflation"],["Deflation"],["Stagflation"],["Reflation"]],
[["Vir Chakra"],["Param Vir Chakra"],["Ashok Chakra"],["Mahavir Chakra"]],
[["Andaman Islands"],["Nicobar Islands"],["Lakshadweep"],["Minicoy"]],
[["Percolation"],["Conduction"],["Leaching"],["Transpiration"]],
[["Conduction"],["Convection"],["Radiation"],["Both conduction and convection"]],
[["Bacteria"],["Virus"],["Fungus"],["Protozoa"]],
[["Japan"],["China"],["USA"],["Russia"]],
[["Rajasthan"],["Uttar" ,"Pradesh"],["Andhra Pradesh"],["Karnataka"]],
[["RBI"],["SEBI"],["Ministry" ,"of" ,"Finance"],["FIPB"]],
[["Loss due to insect pests"],["Decrease in food production"],["Deficiencies of micronutrients and vitamins"],["Loss due to plant diseases"]],
[["Parliament"],["Supreme Court of India"],["President"],["Attorney General of India"]]
]

#Parsing
ps = PorterStemmer()
lmtzr = WordNetLemmatizer()

for i in range(len(questions)):
	questions[i] = parser(questions[i][0], ps, lmtzr)

for i in range(len(options_all)):
	for j in range(len(options_all[i])):
		options_all[i][j] = parser(options_all[i][j][0], ps, lmtzr)

for i in range(len(answers)):
	answers[i] = parser(answers[i][0], ps, lmtzr)

# p = predict(questions[5],options_all[5])
# if(answers[5] == options_all[5][p]):
# 	print("Correct")
# else:
# 	print("Incorrect")

num = 0
for i in range(len(answers)):
	p = predict(questions[i],options_all[i])
	print('The predicted answer is ', p)
	if(answers[i] == options_all[i][p]):
		num += 1
print("% Correct = ", num/len(answers)*100)
	

				