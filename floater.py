# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random #check if okay



class Floater(Prey): 
    
    def __init__(self,x,y,width=10,height=10,angle=None,speed=5):
        Prey.__init__(self,x,y,width,height,angle,speed)
        self.randomize_angle()
        self._image = PhotoImage(file='ufo.gif')
         
        
    def update(self, model): # check if okay
        self.move()
        r = random.random()
        if 0<= r <= .29:
            while True:
                x = random.uniform(-.5, .5)
                if 3 <= self._speed + x <= 7:
                    self._speed += x
                    self._angle += x
                    break
                    
            
    
    def display(self, canvas):
        canvas.create_image(*self.get_location(), image=self._image)
