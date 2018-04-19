import numpy as np
from scipy.special import logit

Data = np.genfromtxt('data.csv', delimiter=',')

# Dict to store response time for each category
response_time = {}
# Dict to store response time for each category
choices = {}
drift = {}
T_nd = {}
seperation = {}
P_c = {}
s = .1
categories = [1,2,3,4]
resp_for_cat = { 1 : 0, 2 : 0, 3 : 1, 4 : 1}

for category in categories:
    response_time[category] = []
    choices[category] = [] 
    P_c[category] = 0.0
for i in range(len(Data[:,0])):
    category = Data[i,0]
    response_time[category].append(Data[i, 2])
    choices[category].append(Data[i, 1])

for i in categories:
    N = 0
    for n in range(len(choices[i])):
        if choices[i][n] == resp_for_cat[i]:
            P_c[i]+=1
        N+=1
    P_c[i] /= N
        
for i in categories:
    sgn = P_c[i] - .5
    tn = P_c[i]*P_c[i]*logit(P_c[i]) - P_c[i]*logit(P_c[i]) + sgn
    td = np.var(response_time[i])
    t = logit(P_c[i])*tn/td
    drift[i] = np.sign(sgn)*s*np.power(t,.25)
    seperation[i] = s*s*logit(P_c[i])/drift[i]
    va_s2 = seperation[i]*drift[i]/(s*s)
    T_nd[i] = np.mean(response_time[i]) - seperation[i]/(2*drift[i])*(1-np.exp(-va_s2))/(1+np.exp(-va_s2))

for category in categories:
    print('Category{}-> \n Drift: {} \n Separation: {} \n Time_nd : {}'.format(category, drift[category], seperation[category],T_nd[category]))
