from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import random
import time
from functools import partial

class Main:
    def __init__(self):
        self.tk = Tk()
        self.tk.title('Paint')
        self.tk.resizable(0,0)
        self.tk.wm_attributes('-topmost',1)


        self.canvas = Canvas(self.tk,width = 600,height = 600)
        self.canvas.pack()


        self.canvas.create_rectangle(-1,-1,1000,1000,fill = 'white',outline = 'white')


        self.edit_colour_button = self.canvas.create_rectangle(5, 5, 35, 35, fill = 'red', outline = 'blue')
        self.erase_button = self.canvas.create_rectangle(5, 40, 35, 70, fill = 'snow', outline = 'black')
        self.edit_colour_text = self.canvas.create_text(20,20,font = ('Book Antiqua',7),fill = 'yellow',text = '''  Edit
Colour''')
        self.erase_text = self.canvas.create_text(20,55,font = ('Book Antiqua',8),text = 'Erase')
        
        self.canvas.tag_bind(self.edit_colour_button, '<Button-1>', self.edit_colour)
        self.canvas.tag_bind(self.edit_colour_text,'<Button-1>', self.edit_colour)
        self.canvas.tag_bind(self.erase_button,'<Button-1>', partial(self.finalize_colour,colour = 'white'))
        self.canvas.tag_bind(self.erase_text,'<Button-1>', partial(self.finalize_colour,colour = 'white'))
        
        
        self.colours_for_column1 = ['black', 'blue violet', 'maroon', 'blue2', 'green2', 'green4']
        self.colours_for_column2 = ['red', 'gray63', 'yellow', 'orange', 'violetred2', 'royalblue4']
        
        x1 = 40
        x2 = 70
        for x in self.colours_for_column1:
            self.colour_button = self.canvas.create_rectangle(x1, 5, x2, 35, fill = x, outline = x)
            self.canvas.tag_bind(self.colour_button, '<Button-1>', partial(self.finalize_colour,colour = x))
            x1 += 35
            x2 += 35
            
        x1 = 40
        x2 = 70
        for x in self.colours_for_column2:
            self.colour_button = self.canvas.create_rectangle(x1, 40, x2, 70, fill = x, outline = x)
            self.canvas.tag_bind(self.colour_button, '<Button-1>', partial(self.finalize_colour,colour = x))
            x1 += 35
            x2 += 35
            
        x1 = 250
        x2 = x1 + 30
        for x in range(1,4):
            self.resizable_button = self.canvas.create_rectangle(x1, 5, x2, 35,fill = 'black',outline = 'black')
            self.resizable_text = self.canvas.create_text(x1 + 15,20,text = x,font = ('Times',15),fill = 'white')
            self.canvas.tag_bind(self.resizable_button, '<Button-1>', partial(self.pen_size,size = x * 20))
            self.canvas.tag_bind(self.resizable_text, '<Button-1>', partial(self.pen_size,size = x * 20))
            x1 += 35
            x2 += 35
            
        x1 = 250
        x2 = x1 + 30
        for x in range(4,7):
            self.resizable_button = self.canvas.create_rectangle(x1, 40, x2, 70,fill = 'black',outline = 'black')
            self.resizable_text = self.canvas.create_text(x1 + 15,55,text = x,font = ('Times',15),fill = 'white')
            self.canvas.tag_bind(self.resizable_button, '<Button-1>', partial(self.pen_size,size = x * 20))
            self.canvas.tag_bind(self.resizable_text, '<Button-1>', partial(self.pen_size,size = x * 20))
            x1 += 35
            x2 += 35
        self.new_button = self.canvas.create_rectangle(355, 40, 600, 70,fill = 'black')
        self.new_text = self.canvas.create_text(475,55,text = 'New',font = ('Helvetica',15),fill = 'white')

        self.canvas.tag_bind(self.new_button,'<Button-1>',self.new)
        self.canvas.tag_bind(self.new_text,'<Button-1>',self.new)
        
        self.clear_button = self.canvas.create_rectangle(355, 5, 600, 35,fill = 'black')
        self.clear_text = self.canvas.create_text(475,20,text = 'Clear',font = ('Helvetica',15),fill = 'white')

        self.canvas.tag_bind(self.clear_button,'<Button-1>',self.clear)
        self.canvas.tag_bind(self.clear_text,'<Button-1>',self.clear)
            
            
        self.colour = 'black'



        self.size = 20
    def edit_colour(self,evt):
        c = colorchooser.askcolor(0)[1]
        self.finalize_colour(colour = c)
    def finalize_colour(self,evt = None,colour = None):
        self.colour = colour
    def pen_size(self,evt,size):
        self.size = size
    def new(self,evt):
        m = Main()
        p = Pen(m)
    def clear(self,evt):
        self.canvas.create_rectangle(0,71,601,601,fill = 'white',outline = 'white')




class Pen:
    def __init__(self,m):
        self.m = m
        self.m.canvas.bind_all('<B1-Motion>',self.draw)
    def touching_buttons(self):
        y = self.m.canvas.winfo_pointery() - self.m.canvas.winfo_rooty()
        if y < 75:
            return True
        return False
    def draw(self,evt):
        if self.touching_buttons() == False:
            color = self.m.colour
            x = self.m.canvas.winfo_pointerx() - self.m.canvas.winfo_rootx()
            y = self.m.canvas.winfo_pointery() - self.m.canvas.winfo_rooty()
            self.m.canvas.create_oval(x,y, x + self.m.size, y + self.m.size , fill = color, outline = color)
            self.m.tk.update()


        
        
        
    
            
            
m = Main()
p = Pen(m)
m.tk.mainloop()
