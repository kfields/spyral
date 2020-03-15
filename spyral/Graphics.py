
from pyglet.gl import *

class Graphics():
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.color=(255.,255.,255.,1.)
        self.stroke = 1
        self.q = gluNewQuadric()
        
    def translate(self, x, y, z = 0):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z
        
    def set_color(self,c):
        self.color = c
        
    def start_draw(self):
        glColor4f(*self.color)
        glPushMatrix()
        glTranslatef(self.x, self.y, self.z)
        #glRotatef(self.rotation, 0, 0, 0.1)
        
    def end_draw(self):
        glPopMatrix()
    
    def fill_rect(self, x, y, width, height):
        glRectf(x, y, width, height)
    
    def draw_point(self, x, y, z = 0):
        self.start_draw()        
        glBegin(GL_POINTS) # draw point
        glVertex3f(x, y, z)
        glEnd()
        self.end_draw()
        
    def draw_circle(self, x, y, z, radius):
        """ Draw Circle
            x, y, z, width in pixel, rotation, color and line width in px
            style choices are : GLU_LINE, GLU_FILL, GLU_SILHOUETTE, GLU_POINT
            TO DO : textured circles
        """
        self.start_draw()

        if radius < 1 : radius = 1

        if self.stroke :
            inner = radius - self.stroke # outline width
            if inner < 0: inner=0
        else :
             inner = 0 # filled
        
        gluQuadricDrawStyle(self.q, GLU_LINE)

        circleresolution = 60
        gluDisk(self.q, inner, radius, circleresolution, 1) # gluDisk(quad, inner, outer, slices, loops)
            
        self.end_draw()
    
    def draw_line(self, x1, y1, x2, y2):
        self.start_draw()
        if self.stroke <= 0:
            self.stroke = 1
        glLineWidth(self.stroke)

        glBegin(GL_LINES)
        glVertex2f(x1, y1) # draw pixel points
        glVertex2f(x2, y2)
        glEnd()
        self.end_draw()
        
        