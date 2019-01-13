#!/usr/bin/python 

# Machine Learning for ShortStocks

from sklearn.neural_network import MLPClassifier
import getall
	
full = getall.getall("Navya")

X = full[0]

y = full[1]


clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 40, 10, 2), random_state=1)

clf.fit(X, y)

print(clf.predict([[2, 0]]))






    




