#images.py
#By Sun Hao

from graphics import*
from math import*
class images:
    
    def __init__(self):
        1
   
    def star(self,window,center,size,color):
        self.center=center
        
        p1=center.clone()
        p1.move(0,+size)
        p2=center.clone()
        p2.move(size*cos(18*pi/180),size*sin(18*pi/180))
        p3=center.clone()
        p3.move(size*cos(-54*pi/180),size*sin(-54*pi/180))
        p4=center.clone()
        p4.move(-size*cos(54*pi/180),size*sin(-54*pi/180))
        p5=center.clone()
        p5.move(-size*cos(18*pi/180),size*sin(18*pi/180))

        self.Star=Polygon(p1,p3,p5,p2,p4,p1)
        self.Star.setFill(color)
        self.Star.draw(window)

    def circle(self,window,center,size,color):
        self.c=Circle(center,size)
        self.c.setFill(color)
        self.c.draw(window)

    def cirstar(self,window,center,size,colorstar,colorcircle):
        self.circle(window,center,size,colorcircle)
        self.star(window,center,size,colorstar)

    def undraw(self,stuff):
        if stuff=="star":
            self.Star.undraw()
        elif stuff=="circle":
            self.c.undraw()
        elif stuff=="cirstar":
            self.Star.undraw()
            self.c.undraw()

    def draw(self,window,stuff):
        if stuff=="star":
            self.Star.draw(window)
        elif stuff=="circle":
            self.c.draw(window)
        elif stuff=="cirstar":
            self.Star.draw(window)
            self.c.draw(window)
        

    def moving(self,stuff,dx,dy):
        if stuff=="star":
            self.Star.move(dx,dy)
        elif stuff=="circle":
            self.c.move(dx,dy)
        elif stuff=="cirstar":
            self.Star.move(dx,dy)
            self.c.move(dx,dy)

        
        
