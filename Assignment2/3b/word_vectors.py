import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
# X = np.load('wwMat.np')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pickle
from parser import parser
from nltk.stem.porter import PorterStemmer

def load_obj(name ):
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)

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



D = 25
X = np.load('wwMat.npy')
# np.matrix([1,2,3,4,214,123,22,123,1,3,14,2,12,4,2,12,123,2,312,3,12,424,353,34]).reshape((3,8))
pca = PCA(n_components=D, svd_solver='full')
pca.fit(X)
word_embeddings = pca.transform(X)
n_word_embeddings = StandardScaler().fit_transform(word_embeddings)

word_ids = load_obj("word_ids")
ps = PorterStemmer()
lmtzr = WordNetLemmatizer()

q_emd = []
for question in questions:
	question = parser(question[0], ps, lmtzr)
	emb = np.zeros(D)
	n = 0
	for word in question:
		n+=1
		emb +=  n_word_embeddings[word_ids[word],:]
	emb = emb/n
	q_emd.append(emb)

op_emd = []
for options in options_all:
	this_op_emd = []
	for option in options:
		option = parser(option[0], ps, lmtzr)
		emb = np.zeros(D)
		n=0
		for word in option:
			n+=1
			emb +=  n_word_embeddings[word_ids[word],:]
		this_op_emd.append(emb/n)	
	op_emd.append(this_op_emd)

q_no = 0
pred_answers = []
for i in range(len(q_emd)):
	min_d = np.inf 
	j = 0
	answer = -1
	for option in options_all[i]:
		dist = np.linalg.norm(op_emd[i][j]-q_emd[i])
		if(dist<min_d):
			answer = j
			min_d = dist 
		j+=1
	pred_answers.append(answer)

cor = 0.0
for i in range(len(pred_answers)):
	if(options_all[i][pred_answers[i]] == answers[i]):
		cor+=1

print("Accuracy is {0}".format(cor*100/len(pred_answers)))