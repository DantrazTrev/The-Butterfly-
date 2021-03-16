import numpy as np 
from backpropogation import backprop
import json 

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
            a = sigmoid(np.dot(w, a)+b)
            out.append(a)  
        nabw=[]
        for j,i in zip(out[1:],out[:-1]):
          nabw.append(np.dot(i,np.transpose(j)).transpose())
       
        #implement forgetting factor
        self.weights=[w+eta*nw  for w,nw in zip(self.weights,nabw)]  
        #check the bias update
        self.biases=[b+eta*nw for b,nw in zip(self.biases,out[1:])]
        
        #Implement Hebbian interface
        

  # reverse traversal
  #Still needs research , Current implementation is just inverse of sigmoid
    def rev(self,op):
      wr=np.flip(self.weights)
      br=np.flip(self.biases)
      reverse=list(zip(br,wr))
      print(reverse)
      for b,w in reverse:
        op=op-b
        op=inv_sigmoid(np.dot(np.transpose(w),op))
        print(op)
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
        self.weights = [w-(eta/(len(mini_batch)+1))*nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b-(eta/len(mini_batch))*nb
                       for b, nb in zip(self.biases, nabla_b)]

    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
   
    def cost_derivative(self, output_activations, y):
        return (output_activations-y)
    
    def save(self):
        data = {"sizes": self.sizes,
                "weights": [w.tolist() for w in self.weights],
                "biases": [b.tolist() for b in self.biases]}
        return data
   
    def load(self,data):
      self.weights = [np.array(w) for w in data["weights"]]
      self.biases = [np.array(b) for b in data["biases"]]
          
def sigmoid(z):
      return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
      return sigmoid(z)*(1-sigmoid(z))    
def inv_sigmoid(z):
  return sigmoid(z)
 #To be left for discussion over inverse sigmoid function , Currently only using sigmoid