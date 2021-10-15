#MINI SMART CALCULATOR SOFTWARE CODE with time and date
from math import *
expression=["Welcome to Smart calculator ","Thank You","Sorry This is beyond my ability","Somethig  wromg plze Try again","My name is Maurya","Hello"]
l=[]
def time() :
    import datetime
    now = datetime.datetime.now()
    print ("Current Time is",now.strftime("%H:%M"))

def date():
    from datetime import date
    today = date.today()
    print("Today's date:", today)
def hello() :
    print(expression[5])

def lcm(l):
   m=max(l)
   while(True) :
       if(all([m%e==0 for e in l])) :
           return m
       m+=1

def Hcf(l):
    m=min(l)
    if(all([e%m==0 for e in l])) :
        return m
    m-=1
   

def sum(l) :
    s=0
    for e in l :
        s+=e
    return s
def sub(l) :
    return l[0]-l[1]
def multiply(l) :
    r=1
    for e in l :
        r*=e
    return r
def division(l) :
    return l[0]/l[1]
def end():
   print(expression[1])
   input("Press Enter key to exit")
   exit()
def sorry() :
    print(expression[2])
def  myname() :
    print(expression[4])
def extract_no(w) :
    l=[]
    for e in w.split() :
        try :
           l.append(float(e))
   
        except :
            pass  
    return l
def last() :
    pass
operation={"ADDITION":sum,"SUM":sum,"ADD":sum,"PLUS":sum,"SUBTRACTION":sub,"SUBTRACT":sub,"MINUS":sub,"MULTIPLY":multiply,"MULTIPLICATION":multiply,"PRODUCT":multiply,
           "MULTIPLIED":multiply,"MUL":multiply,"DIVISION":division,"DIVIDE":division,"DIVIDED":division,"DIV":division,"LCM":lcm,"HCF":Hcf,"LAST":last }
command={"END":end,"EXIT":end,"CLOSE":end,"NAME":myname,"YOURNAME":myname,"DATE":date,"TIME":time,"HII":hello,"HEY":hello,"HELLO":hello,"HII":hello}
print(expression[0])
while True :
  x=input("Enter sum text")
  y=x
  for e in x.split(' ') :
     if e.upper() in operation.keys() :
         try :
             L=extract_no(x)
             r=operation[e.upper()](L)
             print(r)
             break
         except :
             print("something is Wrong")
             break
     elif e.upper() in command.keys() :
         command[e.upper()]()
         break
  else :
      if ' ' not in y :
          try :
             print(eval(y))
          except :
              print("Invalid formate")
             
      else :
        sorry()
