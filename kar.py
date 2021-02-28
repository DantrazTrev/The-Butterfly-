# Interface for the butterfly
import NN
import numpy as np
from random import *

#Define Charactaers as an array to be intialized with the Player object
Chaure=[]

def ipply():
  ip=[]
  for j in Chaure:
    ip.append(ops(ip))
class Player:
#additional parameters
  def _init_(self,chaur,choices,level,id):
    size=[chaur+1]
    Chaure = [0]*(chaur+1)
    for i in range(level):
      size.append(randint(3,chaur)) #needs to be tested and updated
    size.append(choices)
    self.net=NN.Network(size)
    self.id=chaur
    Chaure[chaur]=self
  def ips(self):
    ip=[]
    for jane in range(size[0]):
      ip.append(chars.output())
    ip.append(self.output())
    return ip
  def influenced(self,ips,trust,forget):
    #inputs to be gathered
      self.hebbian(ips,trust,forget)
  def ops(self,ips):
    self.net.feedforward(ips)      
  def trusts(self):   #trust matrix
    tmatrix=[self.net.wieghts[0]]
    return tmatrix
  def forget_factor(self,id):
    meets=0
    for i in Chaure:
      meets=meets+Chaure.freq
    ff=1-(Chaure[id].freq/me)
    Chaure.ff=ff
    return ff

class Others:
  def _init_(self,id,choices,complexity,trust_matrix,trust_level=randint(0,1),freq=randint(30,100)):
    self.trust=trust_level # defines trust level for the charecter from the player
    self.f=freq
    size=[]
    size.append(choices)
    self.id=id
    for jane in range(complexity):
      size.append(randint(4,6)) #random choice till now 
    self.net(size)
    self.tmatrix=trust_matrix
    Chaure[id]=self
    self.ff=randint(0,1);
    # Create a set to train the O-/P to Set one

  def trusts(self,id): #defines how much a chars trusts other
      return self.tmatrix[id]
    
    # For a bipolar output
  def influenced(self,pay_ips,trust,):
    self.net.hebbian(pay_ips,trust,self.ff)
  def ops(a):
    return self.feedforward(a)  
  def influences(self,id):
    chau.influenced(Chaure[id].ops(),tmatrix[id],Chau[id].ff) # need to work out on the forget factor