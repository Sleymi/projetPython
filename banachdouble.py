from tkinter import *
from random import randrange

 
 
 
def prog6():

 
 def changecolor():
 
  c=randrange(8)
  couleur=['purple','white','red','blue','green','black','yellow','maroon']
  coul=couleur[c]
  return coul
 

 def tracer():
  can.delete(ALL)   
  
  
  def t(a,b,h):
   
   
   x,y,r=a,b,h
   #can.create_rectangle(x,y,x+r,y+r,width=2,fill='yellow',outline="blue")

   #can.create_oval(x,y,x+r,y+r,width=2,fill='yellow',outline="blue")

   can.create_line(x,y,x+r,y+r,width=2,fill=changecolor())
   #can.create_arc(x,y,x+r,y+r,width=2,fill='yellow',outline="blue")
  
  
   
   
  n=taille=entr1.get()
  n=int(n)
   
  
  
  def f2(n,h,a,b):
   
   if(n==0): 
    t(a,b,h)
   

       
    
   elif n>0:
    f2(n-1,h/2,a,b)
    f2(n-1,h/2,a+h/2,b)
    f2(n-1,h/2,a+h/4,b+h/2)
  def f(n,h,a,b):
   
   if(n==0): 
    t(a,b,h)
   

       
    
   elif n>0:
    f(n-1,h/2,a+h/4,b)
    f(n-1,h/2,a+0,b+h/2)
    f(n-1,h/2,a+h/2,b+h/2) 
  
  f(n,300,0,0)
  f2(n,300,0,300)
 
  """  
  f(n,200,0,0)
  f(n,200,200,0)
  f(n,200,200,200)
  f(n,200,0,200)
  """
  #f(n,400,0,200) 
  
  
    
 global f
 f=Tk()
 can=Canvas(f,bg='green',height=600,width=300)
 photo = PhotoImage(file ='a.gif')
 item = can.create_image(150, 150, image =photo)
 can.pack()
 
 entr1 = Entry(f)
 entr1.pack()
 b=Button(f,text='Afficher',command=tracer)
 b.pack()
prog6();
