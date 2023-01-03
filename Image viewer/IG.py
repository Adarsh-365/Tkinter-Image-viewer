from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.geometry()
canvas = Canvas(root, width=1000, height=600)
canvas.grid(column=0,row=0)
canvas.create_rectangle(599,99,900,400,fill='red')
root.title("Imges")

##################

#######################
image_no_1 = ImageTk.PhotoImage(Image.open("1.jpg").resize((60,60)))
image_no_2 = ImageTk.PhotoImage(Image.open("2.jpg").resize((60,60)))
image_no_3 = ImageTk.PhotoImage(Image.open("3.jpg").resize((60,60)))
image_no_4 = ImageTk.PhotoImage(Image.open("4.jpg").resize((60,60)))
image_no_5 = ImageTk.PhotoImage(Image.open("5.jpg").resize((60,60)))
image_no_6 = ImageTk.PhotoImage(Image.open("6.jpg").resize((60,60)))
image_no_7 = ImageTk.PhotoImage(Image.open("7.jpg").resize((60,60)))
image_no_8 = ImageTk.PhotoImage(Image.open("8.jpg").resize((60,60)))
image_no_9 = ImageTk.PhotoImage(Image.open("9.jpg").resize((60,60)))
image_no_10 = ImageTk.PhotoImage(Image.open("10.jpg").resize((60,60)))
image_no_11= ImageTk.PhotoImage(Image.open("11.jpg").resize((60,60)))
image_no_12= ImageTk.PhotoImage(Image.open("12.jpg").resize((60,60)))
image_no_13 = ImageTk.PhotoImage(Image.open("13.jpg").resize((60,60)))
image_no_14 = ImageTk.PhotoImage(Image.open("14.jpg").resize((60,60)))
image_no_15 = ImageTk.PhotoImage(Image.open("15.jpg").resize((60,60)))
image_no_16 = ImageTk.PhotoImage(Image.open("16.jpg").resize((60,60)))
image_no_17 = ImageTk.PhotoImage(Image.open("17.jpg").resize((60,60)))
image_no_18 = ImageTk.PhotoImage(Image.open("18.jpg").resize((60,60)))
image_no_19 = ImageTk.PhotoImage(Image.open("19.jpg").resize((60,60)))
image_no_20 = ImageTk.PhotoImage(Image.open("20.jpg").resize((60,60)))


    



image_no__10 = ImageTk.PhotoImage(Image.open("1.jpg"))
image_no__20 = ImageTk.PhotoImage(Image.open("2.jpg"))
image_no__30 = ImageTk.PhotoImage(Image.open("3.jpg"))
image_no__40 = ImageTk.PhotoImage(Image.open("4.jpg"))
image_no__50 = ImageTk.PhotoImage(Image.open("5.jpg"))
image_no__60 = ImageTk.PhotoImage(Image.open("6.jpg"))
image_no__70 = ImageTk.PhotoImage(Image.open("7.jpg"))
image_no__80 = ImageTk.PhotoImage(Image.open("8.jpg"))
image_no__90 = ImageTk.PhotoImage(Image.open("9.jpg"))
image_no__100 = ImageTk.PhotoImage(Image.open("10.jpg"))
image_no__110 = ImageTk.PhotoImage(Image.open("11.jpg"))
image_no__120 = ImageTk.PhotoImage(Image.open("12.jpg"))
image_no__130 = ImageTk.PhotoImage(Image.open("13.jpg"))
image_no__140 = ImageTk.PhotoImage(Image.open("14.jpg"))
image_no__150 = ImageTk.PhotoImage(Image.open("15.jpg"))
image_no__160 = ImageTk.PhotoImage(Image.open("16.jpg"))
image_no__170 = ImageTk.PhotoImage(Image.open("17.jpg"))
image_no__180 = ImageTk.PhotoImage(Image.open("18.jpg"))
image_no__190 = ImageTk.PhotoImage(Image.open("19.jpg"))
image_no__200 = ImageTk.PhotoImage(Image.open("20.jpg"))





class MouseMover():
  def __init__(self):
    global image_no_10
    self.List_images = [image_no_1, image_no_2, image_no_3, image_no_4,image_no_5,
                        image_no_6,image_no_7,image_no_8,image_no_9,image_no_10,image_no_11,image_no_12
                        ,image_no_13, image_no_14,image_no_15,
                        image_no_16,image_no_17,image_no_18,image_no_19,image_no_20,]
    self.List_imagesb = [image_no__10, image_no__20, image_no__30, image_no__40,image_no__50,
                        image_no__60,image_no__70,image_no__80,image_no__90,image_no__100,image_no__110,image_no__120,
                         image_no__130, image_no__140,image_no__150,
                                            image_no__160,image_no__170,image_no__180,image_no__190,image_no__200]
    self.item = 0; self.previous = (0, 0)
    a=10
    b=10
    for i in range(1,21,1):
        print(i)
        
        t='img'+str(i)
        
        canvas.create_image(a,b,anchor=NW,image=self.List_images[i-1],tags=('sm',t))
        a=a+70
        if a==500:
            a=10
            b=b+70
  def select(self, event):
    widget = event.widget                       
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    self.item = widget.find_closest(xc, yc)[0]        # ID for closest
    self.previous = (xc, yc)
    if self.item !=1:
        canvas.lift(self.item)
    tag1=canvas.gettags(self.item)
    if self.item !=1:
       
            a=10
            b=10
            
            for i in range(1,21,1):
                wow='img'+str(i)
                k=i
                if tag1[1]==wow:
                    a=70*(k-1)+ 10
                    print(a)
                    if a>=500:
                        if a>950:
                            k=k-7
                            b=b+70
                        
                        k=k-7
                        print(k)
                        a=70*(k-1)+ 10
                        b=b+70
                    
                    n=canvas.create_image(a,b,anchor=NW,image=self.List_images[i-1],tags=('sm',wow))
                    canvas.lower(n)
                    
         
    print((xc, yc, self.item))
  def realse(self,event):
      widget = event.widget 
      xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
      self.newi=canvas.gettags(self.item)
     
      
      print((xc, yc, self.item))
      tag1=canvas.gettags(self.item)
      print(tag1)
      ##################################################
      newi=canvas.coords(self.item)
      print(newi)
      xc1=newi[0]
      yc1=newi[1]
      if tag1:
          if tag1[0]=='sm':
              
               if (xc1>=600 and yc1>=100 and xc1<=880 and yc1<=380):
                   
                   
                   a=10
                   b=10
                   for i in range(1,21,1):
                       wow='img'+str(i)
                       
                       k=i
                       if tag1[1]==wow:
                           a=70*(k-1)+ 10
                           print(a)
                           if a>=500:
                               if a>950:
                                   k=k-7
                                   b=b+70
                               k=k-7
                               print(k)
                               a=70*(k-1)+ 10
                               b=b+70
                           canvas.delete(self.item)    
                           canvas.create_image(600,100,anchor=NW,image=self.List_imagesb[i-1],tags='big')
                           canvas.create_image(a,b,anchor=NW,image=self.List_images[i-1],tags=('sm',wow))
                           
                       
      
      
      
      
      
      
      
      #######################################################
     
               elif( xc1<600 or yc1<100 or xc1>880 or yc1>380):
                   a=10
                   b=10
                   
                   for i in range(1,21,1):
                       wow='img'+str(i)
                       k=i
                       if tag1[1]==wow:
                           a=70*(k-1)+ 10
                           print(a)
                           if a>=500:
                               if a>950:
                                   k=k-7
                                   b=b+70
                               k=k-7
                               print(k)
                               a=70*(k-1)+ 10
                               b=b+70
                           canvas.delete(self.item)
                           canvas.create_image(a,b,anchor=NW,image=self.List_images[i-1],tags=('sm',wow))
                           
                
                        
  def drag(self, event):
      
    widget = event.widget
    xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
    tagg=canvas.gettags(self.item)
   
    if self.item !=1:
        
           
            if tagg[0]!='big':
                canvas.move(self.item, xc-self.previous[0], yc-self.previous[1])
                self.previous = (xc, yc)

            
# Get an instance of the MouseMover object
mm = MouseMover()

# Bind mouse events to methods (could also be in the constructor)
canvas.bind("<Button-1>", mm.select)
canvas.bind("<ButtonRelease-1>", mm.realse)
canvas.bind("<B1-Motion>", mm.drag)



root.mainloop()