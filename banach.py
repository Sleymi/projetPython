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
   #can.create_rectangle(x,y,x+r,y+r,width=2,fill='yellow',outline="yellow")

   #can.create_oval(x,y,x+r,y+r,width=2,fill='yellow',outline="yellow")

   can.create_line(x,y,x+r,y+r,width=2,fill='yellow')
   #can.create_arc(x,y,x+r,y+r,width=2,fill='yellow',outline="blue")
  
  
   
   
  n=taille=entr1.get()
  n=int(n)
   
  
  
  
  def f(n,h,a,b):
   
   if(n==0): 
    t(a,b,h)
   

       
    
   elif n>0:
    f(n-1,h/2,a+h/4,b)
    f(n-1,h/2,a+0,b+h/2)
    f(n-1,h/2,a+h/2,b+h/2) 
  
  f(n,400,0,0)
  """  
  f(n,200,0,0)
  f(n,200,200,0)
  f(n,200,200,200)
  f(n,200,0,200)
  """
  #f(n,400,0,200) 
  
  
    
 global f
 f=Tk()
 can=Canvas(f,bg='red',height=400,width=400)

 can.pack()
 
 entr1 = Entry(f)
 entr1.pack()
 b=Button(f,text='test',command=tracer)
 b.pack()
