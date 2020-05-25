#!/usr/bin/python

'''
https://www.python.org/dev/peps/pep-0008/
'''


class DSELinearClassifier():
    
    def __init__(self,activation=None,random_state=None, learning_rate=None):
        self.activation = activation
        self.random_state = random_state
        self.learning_rate = learning_rate
        
        if self.activation == 'AdalineGD':
            from AdalineGD import AdalineGD
            print("Your activation is AdalineGD")
            self.classifier = AdalineGD(eta=self.learning_rate,random_state=self.random_state)
        elif self.activation == 'HyperTan':
            from HyperTan import HyperTan
            print("Your activation is HyperTan")
            self.classifier = HyperTan(eta=self.learning_rate,random_state=self.random_state)
        else:
            from Perceptron import Perceptron
            self.activation = 'Perceptron'
            print("Your activation is defaulted to Perception. You can set the activation argument to 'AdalineGD' or 'HyperTan'")
            self.classifier = Perceptron(eta=self.learning_rate,random_state=self.random_state)
        
        return
    
    def fit(self,X,y):
        return self.classifier.fit(X,y)