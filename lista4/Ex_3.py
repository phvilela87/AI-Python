
import numpy as np
import cmath
#import scipy as sp
#from scipy.special import erfc
#from sklearn.naive_bayes import GaussianNB
#import matplotlib.pyplot as plt

X = np.array([[1.83,81.65,30.48],
[1.80,86.18,27.94],
[1.70,77.11,30.48],
[1.80,74.84,25.40],
[1.52,45.36,15.24],
[1.68,68.04,20.32],
[1.65,58.97,17.78],
[1.75,68.04,22.86]])

y = np.array(['masculino','masculino','masculino','masculino','feminino','feminino','feminino','feminino'])

# Instantiate a Gaussian naive Bayes classifier.
#gnb = GaussianNB()

# fit.
#gnb.fit(X, y)

# Predict.
#print('Resposta: sexo %s' % gnb.predict([[1.83,58.97,20.32]])[0])

#print(gnb.predict_proba([[1.83,58.97,20.32]]) )


P_fem = 1.0/2.0
P_mas = 1.0/2.0

mu_altura_mas = (X[0:3+1,0].mean())
std_altura_mas = (X[0:3+1,0].std())
P_altura_mas = sp.stats.norm.pdf(1.83, mu_altura_mas, std_altura_mas)
P_altura_mas_X_P_mas = P_altura_mas*P_mas

mu_peso_mas = (X[0:3+1,1].mean())
std_peso_mas = (X[0:3+1,1].std())
P_peso_mas = sp.stats.norm.pdf(58.97, mu_peso_mas, std_peso_mas)
P_peso_mas_X_P_mas = P_peso_mas*P_mas

mu_tam_mas = (X[0:3+1,2].mean())
std_tam_mas = (X[0:3+1,2].std())
P_atm_mas = sp.stats.norm.pdf(20.32, mu_tam_mas, std_tam_mas)
P_atm_mas_X_P_mas = P_atm_mas*P_mas