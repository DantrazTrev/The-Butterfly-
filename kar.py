# Interface for the butterfly
import NN
import numpy as np
from random import *

#Define Charactaers as an array to be intialized with the Neural network as an object
Chaure=[]

#Chaure does it probably
#def ipply():
#  ip=[]
#  for j in Chaure:
#    ip.append(ops(ip))

#Class A template for player
class Player:
#Intialization
#chaur : number of charecters
#choices : number of choices
#level : wil define the complexity of the next
#id : wtf?
  def __init__(self,chaur,choices,level,freq=np.random.randint(10,40)):
    size=[chaur+1]
    for i in range(chaur+1):
      Chaure.append(0)
    for i in range(level):
      size.append(np.random.randint(2,chaur)) #needs to be tested and updated
    size.append(choices)
    self.net=NN.Network(size)
    self.id=chaur
    self.insize=size[0]
    self.osize=size[-1]
    Chaure[chaur]=self
    self.freq=freq
    self.op=[]
    self.ip=[]
#MEing ie turning a player into me (One time only function assumes no other influence )
#ops defines the outputs of other players
#iter defines the number of iterations
#selfcon is the level of confidence ie the learning rate 
#ops are my choices
  def meing(self,ops,selfcon,iter):
    ips=np.zeros((self.net.insize,1))
    ips[-1]=[1]
    data = list(zip([ips],[ops]))
    self.net.QS(data,iter,selfcon)
    self.op=self.net.feedforward(ips)
#Ips ??
  def ips(self):
    global Chaure
    ips=[]
    for jane in Chaure[:-1]:
      ips.append([jane.ops(self.op)])
    ips.append([1])  
      
      
#influenced defines how a player is influneced by someone
#ips is the input
#trust is the trust trust_level
#forget is the forgetting factor
  def influenced(self,id):
    #inputs to be gathered
      global Chaure
      ips=Chaure[id].op# needs to be fixed
      trust =self.trusts(id)
      forget=self.forget_factor(id)
      self.net.hebbian(ips,trust,forget)
      self.op=self.net.feedforward(ips)

  def ops(self,ips):
    
    self.op= self.net.feedforward(ips)
    return self.op
  
  def trusts(self,id):   #trust matrix
    tmatrix=[self.net.weights[0]]
    trusts=[]
    for t in tmatrix:
      trusts.append(sum(t)/len(t))
    return trusts[id]

  def forget_factor(self,id):
    meets=0
    for i in Chaure:
      meets=meets+Chaure.freq
    ff=1-(Chaure[id].freq/meets)
    Chaure.ff=ff
    return ff

  def dicu(self,id):
    global Chaure
    ops=Chaure[id].rev()
    trust=self.trusts(id)
    freq=self.freq[id]
    ips=self.ips()
    ips[id]=[1]
    data=zip([ips],[ops])
    self.net.QS(data,freq,trust)
    self.op=self.ops(ips)



class Others:
  
  def __init__(self,id,choices,complexity,trust_level=np.random.rand(0,1),freq=np.random.randint(30,100)):
    self.trust=trust_level # defines trust level for the charecter from the player
    self.f=freq
    size=[]
    size.append(choices)
    self.id=id
    for jane in range(complexity):
      size.append(np.random.randint(4,6))
     #random choice till now 
    size.append(2)
    self.net(size)
    global Chaure 
    turt=np.random.rand(len(Chaure))
    Chaure[id]=self
    self.tmatrix=turt;
    self.ff=Chaure[-1].forget_factor(id)
    self.op=[]
    self.tb=[]
    # Create a set to train the O-/P to Set one

  def trusts(self,id): #defines how much a chars trusts other
      return self.tmatrix[id]

  #For the love of god complete this(I know that bh)
  def iktb(self,ips,iteration,selfcon=np.random.randn()):
    ops=np.zeros((2,1))
    ops[0]=[1]
    ops=[ops]
    ips=[ips]
    data=list(zip(ips,ops))
    self.net.QS(self.net,data,iteration,selfcon)
    self.op=self.net.feedforward(ips)
    
  def ktb(self):
    ip=self.net.rev(self.op)
    return ip
    # For a bipolar output
    

  def pinfluence(self):
    global Chaure
    pay_ips=Chaure[-1].op
    trust=self.tmatrix[-1]
    self.net.hebbian(pay_ips,trust,self.ff)
    self.op=self.net.feedforward(pay_ips)

  def disc(self):
    global Chaure
    ips=Chaure[-1].op
    ops=[[1],[0]]
    data = list(zip([ips],[ops]))
    trust=self.tmatrix[-1]
    iter=self.f[id]
    self.net.QS(data,iter,trust)
    self.op=self.net.feedforward(ips)

  def ips(self,a=[]):
    if len(a):
      a=self.op
    self.tb= self.net.rev(a)
    return self.tb


  def ops(self,a):
    v=self.net.feedforward(a)  
    s=[(v[0]*1+v[1]*(-1))/2]
    return s  

  def cinfluence(self,id):
    global Chaure
    ips=Chaure[id].ktb()
    influ=self.trusts(id)
    forg=Chaure[id].ff # needs a bit of work 
    self.net.hebbian(ips,influ,forg)
    
