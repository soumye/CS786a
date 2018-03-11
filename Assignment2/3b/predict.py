from computeNGD import computeNGD
import numpy as np

def predict(Question, Options):
	attention = np.zeros(len(Question))
	# print(attention)
	for i in range(len(Question)):
		for j in range(len(Question)):
			if(Question[i] != Question[j]):
				attention[i] += computeNGD(Question[i],Question[j])
				# print(attention[i])
				
	attention[i] = attention[i]/np.sum(attention)
	scores = np.zeros(len(Options))
	for i in range(len(Options)):
		for j in Options[i]: 
			for k in range(len(Question)):
				scores[i] += attention[k]*computeNGD(Question[k],j)		
		scores[i] = scores[i]/len(Options[i]) #Equal attention
		# print(scores)

	return np.argmin(scores)

