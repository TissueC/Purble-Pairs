from images import*
from graphics import*
from time import sleep
class animation:
    def __init__(self):
        1
    def pengpeng(self,window,stuff,center,size,color,dx0,dy0,n):
        Stuff=images()
        if stuff=="star":
            Stuff.star(window,center,size,color)
        elif stuff=="circle":
            Stuff.circle(window,center,size,color)
        elif stuff=="cirstar":
            Stuff.cirstar(window,center,size,color,"green")
        c=center
        dx,dy=dx0,dy0
        for i in range(n):
            if c.getX()>120-size:
                dx=-dx   
            if c.getX()<size:
                dx=-dx     
            if c.getY()>120-size:
                dy=-dy     
            if c.getY()<size:
                dy=-dy    
            Stuff.moving(stuff,dx,dy)
            c.move(dx,dy)
            sleep(0.01)
        Stuff.undraw(stuff)

    def twinkle(self,window,stuff,center,size,color,n):
        Stuff=images()
        if stuff=="star":
            Stuff.star(window,center,size,color)
        elif stuff=="circle":
            Stuff.circle(window,center,size,color)
        elif stuff=="cirstar":
            Stuff.cirstar(window,center,size,color,"green")
        for i in range(n):
            sleep(0.1)
            Stuff.undraw(stuff)
            sleep(0.1)
            Stuff.draw(window,stuff)
        Stuff.undraw(stuff)
    
