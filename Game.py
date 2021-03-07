from kar import *
import random

class Game:
  def __init__(self,id,cux,name="Orta"):
    self.id=id
    self.cu=cux
    if name =="Orta":
      self.name=self.name+str(id)
    else:
      self.name=name
    self.chars=dict()
    self.daycount=0
  
  def start(self,choices,char,level=[]):
    ca=len(char)
    co=len(choices)
    self.charli=char
    self.choli=choices
    if len(level)!=ca+1:
      level=[self.cu]*(ca+1)
    self.chars["You"]=Player(ca,co,level[-1])
    for i in range(ca):
      self.char[ca[i]]=Other(i,co,level[i])
    #Charecters Intialized
  
  def utd(self):
    Me=self.chars["You"]
    Nm=self.chars
    order=set(self.charli)
    cie=list(zip(random.shuffle(self.charli),random.shuffle(self.charli)))
    for i in order:
      for j in range(random.randint(2,12)):
        Me.influenced(Nm[i].id)
        Nm[i].pinfluence()
        self.minchange(Nm[i].id)
      for x,y in cie:
        if Nm[x].id != Nm[y].id:
          for bs in range(random.randint(1,12)):
            Nm[x].cinfluence(Nm[y].id)
            Nm[y].cinfluence(Nm[x].id)
    self.day+=1  
    #Some result mech      

  def discu(self,name):
    if name in self.charli and self.day!=0:
      Me=self.chars["You"]
      Op=self.chars[name]
      for i in range(random.randint(3,5)):
        Me.dicu(Op.id)
        Op.disc()
    self.day+=random.random()       
    #Some result mech   

  def pinf(self,name):
    Me=self.chars["You"]
    Nm=self.chars[name]
    for j in range(random.randint(2,12)):
        Me.influenced(Nm.id)
        Nm.pinfluence()

  def fight(self):    
     Nm=self.chars
     Ak=random.randint(4,25)# big numbers
     for i in range(Ak):
      cie=list(zip(random.shuffle(self.charli),random.shuffle(self.charli)))     
      for x,y in cie:
        if Nm[x].id != Nm[y].id:
          for bs in range(random.randint(1,12)):
            Nm[x].cinfluence(Nm[y].id)
            Nm[y].cinfluence(Nm[x].id) 

  def minchange(self,id):
    iddt=self.charli[id]
    se=random.randint()  
    if se>10:
      ip=random.rand(len(self.choli),1)
      iddt.iktb(ip,se,1)
    

  def whome(self,chm,conf,muc):
    Me=self.chars["You"]
    Me.meing(chm,conf,muc)
  
  def hmk(self,name):
    pass

  def tb(self,name,choices,iter=random.randint(3,50)):
    Nm=self.chars[name]
    con=self.hmk(name)
    Nm.iktb(choices,iter,con)

  def cstat(self,name):
    Nm=self.chars[name]
    return Nm.ip([[1],[0]])

  def pstat(self):
    Me=self.chars["You"]
    return Me.op

  def tC(self,name):
    Nm=self.chars[name]
    Me=self.chars["You"]
    t=Nm.ops(Me.op)
    return t

  