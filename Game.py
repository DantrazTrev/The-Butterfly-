from kar import *
from numpy import random
import os
import json
import shutil
from json import JSONEncoder




class Game:
  #POST ja
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
      os.makedirs("char/"+name)
    except:
      try:
        os.rmdir("char/"+name)
        os.makedirs("char/"+name)
      except:
        print("User already exists")

    
  #POST Ja
  def start(self,choices,char,level=[]):
    ca=len(char)
    co=len(choices)
    self.charli=char
    self.choli=choices
    if len(level)!=ca+1:
      level=[self.cu]*(ca+1)
    self.chars["You"]=Player(ca,co,level[-1])
    for i in range(ca):
      self.chars[self.charli[i]]=Others(i,co,level[i])
    print(self.chars)
    for j in self.charli:
      ip=random.rand(len(choices),1)
      self.chars[j].iktb(ip,30,1)  
    self.day=0
    self.save() 
  
    
  #POST  #Charecters Intialized Ja
  def upday(self,v=1):
    for j in range(v):
      self.utd()
    self.day_threshhold=randint(4,10)
    if self.day == int(self.day):
      self.save()
    return{"day":self.day}

  #Unreferetiable 
  def save(self):
    data=dict()
    Nm=self.chars
    for jane in self.charli:
      data[Nm[jane].id]={"net":Nm[jane].net.save(),"op":Nm[jane].op}
    data[len(Nm)-1]={"net":Nm["You"].net.save(),"op":Nm["You"].op}
    name=str(self.day)
    f=open("char/"+self.name+'/'+name,'w')
    json.dump(data,f,cls=NumpyArrayEncoder)
    f.close()
    print("Save performed")
  
  #POST Ja
  def rewind(self,day):
    f = open("char/"+self.name+'/'+str(day), "r")
    data = json.load(f)
    f.close()
    for id in data:
      Chaure[int(id)].net.load(data[id]["net"])
      Chaure[int(id)].op=data[id]["op"]#Needs testing
    self.day=day
    self.day_threshhold=randint(4,10)
    return {"Rewinded":True,"day":day}
    
  

    
  #GET 
  def utd(self):
    Me=self.chars["You"]
    Nm=self.chars
    order=self.charli.copy()
    random.shuffle(order)
    c1=self.charli.copy()
    c2=self.charli.copy()
    random.shuffle(c1)
    random.shuffle(c2)
    inf=dict()
    cie=list(zip(c1,c2))
    for i in order:
      Me.influenced(Nm[i].id)
      for j in range(random.randint(2,7)):
        Nm[i].pinfluence()
        self.minchange(Nm[i].id)
      inf[i]={"effect":max(Me.op)[0],"level":Nm[i].trust}  
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
    if name in self.charli and self.day>0:
      Me=self.chars["You"]
      Op=self.chars[name]
      for i in range(random.randint(3,5)):
        Me.dicu(Op.id)
        Op.disc()
      return {"Charecter":name,"Choices change":Me.op.tolist()}
    else: 
      return {"Charecters":name,"Choice change":0}
        
  
  #GET requests handled @ api/<user>/day
  #   
  def daystat(self):
    res={"day":self.day,"energy":self.day_threshhold}
    return res

  #pOST
  def pinf(self,name):
    Me=self.chars["You"]
    Nm=self.chars[name]
    self.limits()
    for j in range(random.randint(2,12)):
        Me.influenced(Nm.id)
        Nm.pinfluence()
    return {"name":name,"choice":self.choli[np.argmax(Me.op)],"eft":max(Me.op)[0]}

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
     c1=self.charli[:]
     c2=self.charli[:]
     random.shuffle(c1)
     random.shuffle(c2)
     for i in range(Ak):
      cie=list(zip(c1,c2))     
      for x,y in cie:
        if Nm[x].id != Nm[y].id:
          for bs in range(random.randint(1,12)):
            Nm[x].cinfluence(Nm[y].id)
            Nm[y].cinfluence(Nm[x].id) 
     return{"status":"Great you've started a fight"}
  
  #UNREFER UNDO
  def minchange(self,id):
    iddt=self.chars[self.charli[id]]
    se=random.randint(5,21)  
    if se>10:
      ip=random.rand(len(self.choli),1)
      iddt.iktb(ip,se,1)
    
    
  #POST
  def whome(self,chm,conf,muc=random.randint(10,30)):
    Me=self.chars["You"]
    Me.meing(chm,conf,muc)
    return {"status":"Player Config Complete","kar":"You","result":Me.op.tolist()}

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
    acc=acc[0][0]
    me=Nm.ips([[1],[0]])
    me=me.tolist()
    res={self.choli[np.argmax(me)]:max(me)}
    return {"kar":name,"prefers":res,"acceptance":acc}
  
  #POST
  #cehck jane
  def pstat(self):
    Me=self.chars["You"]
    choice=dict()
    for jane in range(len(self.choli)):
      choice[self.choli[jane]]=Me.op[jane][0]
    return {"Playerop":choice}

  def ts(self,name):
    Nm=self.chars[name]
    Me=self.chars["You"]
    t=Nm.ops(Me.op)
    return t

  def quit(self):
    shutil.rmtree("char/"+self.name)
    return {"Game staus":-1}

  def striop(self):
    pass

    #Trust ajust for players

  def trusty(self,name,trust):
    Me=self.chars["You"]
    Nm=self.chars[name]
    Me.trust[Nm.id]=trust
    return {"kar":name,"Action":"Trust Updated"}
    
    #Will never be used
  def fortrusty(self,id,trust):
    Me=self.chars["You"]
    Me.trust[id]+=random.rand(-trust,trust)
  

  #To implement the trust matrix could be dangerous need to add fuzziness to it
  def doawholetrusty(self,tmatrix):
    for jane in len(self.chars)-1:
      self.fortrusty(jane,tmatrix[jane])
    return {"Action":"Trusts Updated"}

    
  def artificialtrusty(self,name):
    Me=self.chars["You"]
    Nm=self.chars[name]
    trust=Me.artificial_trust(Nm.id)
    return {"kar":name,"artrust":trust}
  
    
 #Chnge the freq access point 

  def distancedu(self,name):
    Me=self.chars["You"]
    Nm=self.chars[name]
    f=Nm.freq
    Nm.freq-=random.randint(f/5,f/3)
    return {"kar":name ,"Freq":"reduced"}



  def undistancedu(self,name):
    Me=self.chars["You"]
    Nm=self.chars[name]
    f=Nm.freq
    Nm.freq-=random.randint(f*2,f*5)
    return {"kar":name ,"Freq":"increased"}
      


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)      