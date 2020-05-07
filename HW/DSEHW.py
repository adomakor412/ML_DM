#https://www.python.org/dev/peps/pep-0008/

class DSELinearClassifier():
    
    def __init__(self,activation=None):
        self.activation = activation
        
        if self.activation  == 'Perceptron':
            print("Your activation is Perception")
        elif self.activation == 'AdalineGD':
            print("Your activation is AdalineGD")
        elif self.activation == 'HyperTan':
            print("Your activation is HyperTan")
        elif self.activation not in ['Perceptron','AdalineGD','HyperTan']:
            self.activation = 'Perceptron'
            print("Your activation is defaulted to Perception. You can set the activation argument to 'AdalineGD' or 'HyperTan'")
        
        return