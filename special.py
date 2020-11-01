# Initially starts off as a Pulsator. Once it eats one Prey, Pulsator will turn into a special Hunter than is red(to distinct) and 
# about 1.5 times faster than a normal Hunter but will still decrease size if special Hunter does not eat anything after 30 cycles

from pulsator import Pulsator
from hunter import Hunter

class special(Pulsator):
    def __init__(self, x, y):
        Pulsator.__init__(self, x, y)
    
    def update(self, model):
        x = Pulsator.update(self, model)
        if len(x) != 0:
            new = Hunter(self._x, self._y)
            new._color, new._speed = "red", 7
            model.add(new)
            model.remove(self)
    
        
        
        