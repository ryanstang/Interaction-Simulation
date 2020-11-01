# Black_Hole is singly derived from Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self, x, y, width=Black_Hole.radius*2,height=Black_Hole.radius*2)
        self._color = "black"
        
    def update(self, model):
        result = set()
        for x in model.find(lambda x: isinstance(x, Prey)):
            if self.contains(x.get_location()):
                result.add(x)
                model.remove(x)
        return result
    
    def display(self, canvas):
        dw, dh = self.get_dimension()
        a, b = self.get_location()
        canvas.create_oval(a - dw/2, b - dh/2, 
                           a + dw/2, b + dh/2,
                           fill=self._color)
    
    
    def contains(self, xy):
        return self.distance(xy) < self.get_dimension()[0] / 2