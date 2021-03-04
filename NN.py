import numpy as np 
from backpropogation import backprop
class Network:

    def __init__ (self,size):
      self.insize=size[0]
      self.osize=size[-1]
      self.num_layers=len(size)
    # Needs to be tested ,Can have an alternative of Zero Intitalization
      self.weights= [np.random.randn(y, x)
                        for x, y in zip(size[:-1], size[1:])]
      self.biases= [np.random.randn(y, 1) for y in size[1:]]
  
    def feedforward(self, a):
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a)+b)
        return a
 #Needs work 
    def hebbian(self,input,eta,forget):
        out=[]
        a =input
        out.append(a)
        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, input)+b)
            out.append(a)
        nabw=np.dot(a[1:],a[:-1].T) 
        #implement forgetting factor
        self.weights=[w+eta*nw  for w,nw in zip(self.weights,nabw)]  
        #check the bias update
        self.biases=[b+eta*nw for b,nw in zip(self.biases,nabw)]
        
        #Implement Hebbian interface
        

  # reverse traversal
    def rev(self,op):
      reverse=list(zip(self.biases,self.weights)).reverse()
      for b,w in reverse:
        op=sigmoid(np.dot(w,op)+b)
      return op

    def QS(self,data ,fqu, eta):
        #implement a little deviator 
        for j in range(fqu):
                self.update_mini_batch(data, eta)

    def update_mini_batch(self, mini_batch, eta):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in mini_batch:
            self,delta_nabla_b, delta_nabla_w = backprop(self,x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w-(eta/len(mini_batch))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
   
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
def sigmoid(z):
      return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
      return sigmoid(z)*(1-sigmoid(z))    