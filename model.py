import controller, sys
import model 

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special   import special


running = False
cycle_count = 0
simultons = set()
clicked = ''


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global running, cycle_count, simultons, clicked
    running = False
    cycle_count = 0
    simultons = set()
    clicked = ''


#start running the simulation
def start ():
    global running
    running = True


#stop running the simulation (freezing it)
def stop ():
    global running
    running = False


#step just one update in the simulation
def step ():
    global cycle_count
    if not running:model.start()
    cycle_count += 1
    copy = set(simultons)
    for s in copy:
        if s in simultons:
            s.update(model)
    model.stop()



def select_object(kind):
    global clicked
    clicked = kind 


def mouse_click(x,y):
    global clicked
    if clicked != "Remove":
        model.add(eval(f'{clicked}({x},{y})'))
    else:
        c = set(simultons)
        for s in c:
            if s in simultons:
                if s.contains((x,y)):
                    model.remove(s)
        
#add simulton s to the simulation
def add(s):
    simultons.add(s)
    

# remove simulton s from the simulation    
def remove(s):
    simultons.remove(s)
    

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    result = set()
    for s in simultons:
        if p(s):
            result.add(s)
    return result


#call update \(pass model as its argument\) for every simulton in the simulation

def update_all():
    global cycle_count
    if running:
        copy = set(simultons)
        cycle_count += 1
        for s in copy:
            if s in simultons:
                s.update(model)


def display_all():
    for o in controller.the_canvas.find_all():
        controller.the_canvas.delete(o)
    
    for s in simultons:
        s.display(controller.the_canvas)
    
    controller.the_progress.config(text=str(cycle_count) + " cycles/"+ str(len(simultons)) + " balls")
