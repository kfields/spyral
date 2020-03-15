import sys
import os

sys.path.insert(0, os.path.abspath(__file__))

from spyral.Graphics import Graphics
from spyral.Spyral import Spyral

import pyglet
from pyglet.gl import *

window = pyglet.window.Window()
worldMaxX = 640
worldMaxY = 480
#win = window.Window(worldMaxX, worldMaxY, caption='Wyggles')
g = Graphics()
applet = Spyral(worldMaxX, worldMaxY)


@window.event
def on_draw():
    glClearColor(255.0, 255.0, 255., 1.0)
    window.clear()
    #label.draw()
    applet.paint(g)
    applet.draw_spiral()
    #applet.draw_circle()
    
pyglet.app.run()
