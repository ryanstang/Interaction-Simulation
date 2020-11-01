# Hunter is doubly-derived from the Mobile_Simulton and Pulsator classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    dist = 200
    
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
        Mobile_Simulton.__init__(self, x, y, width=self._width, height=self._height, angle=None, speed=5)
        self.randomize_angle()
        
    def update(self, model):
        self.move()
        Pulsator.update(self, model)
        lst = list()
        for x in model.find(lambda x: isinstance(x, Prey)):
            if self.distance(x.get_location()) <= Hunter.dist:
                lst.append(x)
        if len(lst) != 0:
            a, b = min(lst,key = lambda x : self.distance(x.get_location())).get_location()
            self._x, self._y = self.get_location()
            self.set_angle(atan2(b-self._y, a-self._x))
                
        