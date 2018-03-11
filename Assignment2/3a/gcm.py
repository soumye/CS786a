import scipy.io as sco
import numpy as np

class GCM():
	""" GCM model Class"""
	def __init__(self, exs, Count, alphas, beta, gammas):
		self.alphas = alphas
		self.beta = beta
		self.exs = exs
		self.gammas = gammas
		#dict label,ex
		self.Count = Count 

	def Similarity(self, ex, stimulus):
		distance = 0
		for i in range(len(self.alphas)):
			distance += np.abs(ex[i]-stimulus[i])*self.alphas[i]
		similarity = np.exp(-self.beta*distance)
		return similarity

	def prediction(self, stimulus):
		"""Predicting class for stimulus """
		sum_probs = 0
		probs = np.zeros(len(self.gammas))
		for i in range(len(self.gammas)):
			for j in range(len(self.exs)):
				probs[i]+= self.Count[(j,i+1)]*self.Similarity(self.exs[j], stimulus)
			probs[i] = probs[i]*self.gammas[i]
			sum_probs+= probs[i]
		probs = probs/sum_probs
		#Return label with math probability
		return np.argmax(probs) + 1

#Loading the Data
data = sco.loadmat('height_weight_dataset.mat')
test = np.array(data['y'])
train = np.array(data['X'])
test = np.concatenate((test, np.array([23,11]).reshape((1,2))), axis=0)

#Taking unique data points as exs
exs = np.unique(train[:,:-1],axis=0)
labels = np.unique(train[:,-1],axis=0)
# print(labels)

Count = {} # (ex id, label)
#Count Dictionary For each ex, the number of times it occurs
for i in range(np.shape(exs)[0]):
	for label in labels:
		Count[(i,label)] = 0
	for j in range(np.shape(train)[0]):
		if exs[i,0] == train[j,0] and exs[i,1] == train[j,1]:
			Count[(i,train[i,-1])] += 1

#Defining parameters in accordance with conditions
#More importance to weight than height
alphas = [3,1]
beta = 1
#Gammas reflect prior bias to categories. Biased agains large
gammas = [1,1,.4]
Model = GCM(exs, Count, alphas, beta, gammas)

#Prediction
for i in range(np.shape(test)[0]-1):
	print("\nFor weight : ", test[i,0], " and height : ", test[i,1])
	print("Predicted Class : " , Model.prediction(test[i])) 