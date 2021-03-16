from kar import *
import random
import os
import json
import shutil


class Game:
  #POST
  def __init__(self,id,cux,name="Orta"):
    self.id=id
    self.cu=cux
    if name =="Orta":
      self.name=self.name+str(id)
    else:
      self.name=name
    self.chars=dict()
    self.day_threshhold=random.randint(4,10)
    
    try:
      os.mkdir(name)
    except:
      try:
        os.rmdir(name)
      except:
        print("User already exists")

    
  #POST
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
    self.day=0
    self.save()
    return{"Game Status":1}  
  
    
  #POST  #Charecters Intialized
  def upday(self,v=1):
    self.day+=v
    self.day_threshhold=randint(4,10)
    if self.day == int(self.day):
      self.save()
    return{"day":self.day}

  #Unreferetiable
  def save(self):
    data={}
    Nm=self.chars
    for jane in self.charli:
      data[Nm[jane].id]=Nm[jane].net.save()
      data[Nm[jane].id]={"op":Nm[jane].op}
    data[len(Nm)]=Nm["You"].net.save()
    data[len(Nm)]={"op":Nm["You"].op}
    name=str(self.day)
    f=open(self.name+'/'+name,'w')
    json.dump(data,f)
    f.close()
    print("Save performed")
  
  #POST
  def rewind(self,day):
    f = open(self.name+'/'+str(day), "r")
    data = json.load(f)
    f.close()
    for id in data:
      Chaure[id].net.load(data[id])
      Chaure[id].op=data[id]["op"]#Needs testing
    self.day=day
    self.day_threshhold=randint(4,10)
    return {"Rewinded":True,"day":day}
    
  

    
  #GET
  def utd(self):
    Me=self.chars["You"]
    Nm=self.chars
    order=set(self.charli)
    inf=dict()
    cie=list(zip(random.shuffle(self.charli),random.shuffle(self.charli)))
    for i in order:
      for j in range(random.randint(2,12)):
        res= Nm[i].pinfluence()
        self.minchange(Nm[i].id)
      inf[res["kar"]]={"Choice":res["choice"],"Level":res["inf"]}  
      for x,y in cie:
        if Nm[x].id != Nm[y].id:
          for bs in range(random.randint(1,12)):
            Nm[x].cinfluence(Nm[y].id)
            Nm[y].cinfluence(Nm[x].id)
    self.day+=1
    self.day_threshhold=randint(4,10)
    self.save()
    return inf
    #Some result mech      

  #POST
  def discu(self,name):
    self.limits()
    if name in self.charli and self.day!=0:
      Me=self.chars["You"]
      Op=self.chars[name]
      for i in range(random.randint(3,5)):
        Me.dicu(Op.id)
        Op.disc()
      return {"kar":name,"eft":max(Me.op)[0],"inf":max(Op.tb)[0]}
    else: 
      return {"kar":name,"eft":0,"inf":0}
        
  
  #GET  #Some result mech   
  def daystat(self):
    res={"day":self.day,"energy":self.day_threshhold}

  #pOST
  def pinf(self,name):
    Me=self.chars["You"]
    Nm=self.chars[name]

    self.limits()
    for j in range(random.randint(2,12)):
        Me.influenced(Nm.id)
        Nm.pinfluence()
    return {"name":name,"choice":self.choli[argmax(Me.op)],"eft":max(Me.op)[0]}

  #UNREFER  
  def limits(self):
    if self.day_threshhold<=0:
      self.upday()
    else:
      self.day_threshhold-=1
 
  #GET
  def fight(self):    
     Nm=self.chars
     Ak=random.randint(4,25)# big numbers
     for i in range(Ak):
      cie=list(zip(random.shuffle(self.charli[:-1]),random.shuffle(self.charli[:-1])))     
      for x,y in cie:
        if Nm[x].id != Nm[y].id:
          for bs in range(random.randint(1,12)):
            Nm[x].cinfluence(Nm[y].id)
            Nm[y].cinfluence(Nm[x].id) 
     return{"fight":Ak}
  
  #UNREFER UNDO
  def minchange(self,id):
    iddt=self.chars[id]
    se=random.randint()  
    if se>10:
      ip=random.rand(len(self.choli),1)
      iddt.iktb(ip,se,1)
    
    
  #POST
  def whome(self,chm,conf,muc=random.randint(10,30)):
    Me=self.chars["You"]
    Me.meing(chm,conf,muc)
    return {"kar":"You","result":Me.op}

  def hmk(self,name):
    pass
  
  #POST
  def tb(self,name,choices,iter=random.randint(3,50)):
    Nm=self.chars[name]
    con=self.hmk(name)
    Nm.iktb(choices,iter,con)
    return {"kar":name,"Likely Acceptance":max(choices)[0]}

  #post
  def cstat(self,name):
    Nm=self.chars[name]
    acc=self.ts(name)
    return {"kar":name,"result":Nm.ip([[1],[0]]),"acceptance":acc}
  
  #POST
  
  def pstat(self):
    Me=self.chars["You"]
    choice=dict()
    for jane in range(self.choli):
      choice[self.choli[jane]]=Me.op[jane][0]
    return {"Playerop":choice}

  def ts(self,name):
    Nm=self.chars[name]
    Me=self.chars["You"]
    t=Nm.ops(Me.op)
    return t

  def quit(self):
    shutil.rmdir(self.name)
    return {"Game staus":-1}

  def striop(self):
    pass