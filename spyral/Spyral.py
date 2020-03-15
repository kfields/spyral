import math

from .Graphics import *
from .Color import *

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Spyral():
    def __init__(self, width, height):
        self.width = width ;
        self.height = height ;
        self.preview = False
        self.maxRadius = height/2
        self.spiralColor = Color.black
        
        #self.trackToMax = .5
        self.trackToMax = 1.0
        self.trackRadius = self.maxRadius*self.trackToMax
        
        self.wheelToTrack = .75
        self.wheelRadius = self.trackRadius*self.wheelToTrack
        
        self.holeToWheel = .5
        self.holeRadius = self.wheelRadius*self.holeToWheel
        
        self.calc_radii()

    def calc_radii(self):
        self.trackRadius = self.maxRadius*self.trackToMax
        self.wheelRadius = self.trackRadius*self.wheelToTrack
        self.holeRadius = self.wheelRadius*self.holeToWheel

    def create_graphics(self):
        g = Graphics()
        return g
    
    def clear_view(self):
        g = self.graphics
        g.set_color(Color.white)
        g.fill_rect(0,0,self.width,self.height)
        self.show_preview()

    def show_preview(self):
        self.draw_preview()
        self.preview = True

    def hide_preview(self):
        self.draw_preview()
        self.preview = False

    def draw_preview(self):
        g = self.create_graphics()
        g.translate(self.width/2,self.height/2) ;
        trackRad = self.trackRadius
        wheelRad = self.wheelRadius
        holeRad  = self.holeRadius
        penRad = 5
        trackPoint = Point(-trackRad, -trackRad)
        wheelPoint = Point(-wheelRad, trackRad-(wheelRad*2))
        holePoint = Point(-penRad, (trackRad - wheelRad + holeRad)-penRad)
        
        #g.setXORMode(Color.white) ;
        #g.drawOval(trackPoint.x,trackPoint.y,(int)(trackRadius*2),(int)(trackRadius*2)) ;
        #glEnable(GL_COLOR_LOGIC_OP);
        #glLogicOp(GL_XOR);
        g.set_color(Color.black)
        g.draw_circle(trackPoint.x,trackPoint.y, trackRad*2, trackRad*2)
        #glDisable(GL_COLOR_LOGIC_OP);        
        #g.drawOval(wheelPoint.x,wheelPoint.y,(int)(wheelRadius*2),(int)(wheelRadius*2)) ;
        #g.fillOval(holePoint.x,holePoint.y, penRad, penRad) ;
        #g.setPaintMode() ;

    def draw_circle(self):
        g = self.create_graphics()
        g.set_color(self.spiralColor)
        g.translate(self.width/2,self.height/2) ;
        
        i = 0
        spiralStep = math.pi / 180.0
        oldx = 0
        oldy = 0
        while(i <= 2*math.pi):
            x = 200 * math.cos(i)
            y = 200 * math.sin(i)
            #g.draw_line(oldx, oldy, x, y)
            g.draw_point(x, y)
            oldx = x 
            oldy = y
            i = i + spiralStep
        
    def draw_spiral(self):
        g = self.create_graphics()
        g.translate(self.width/2,self.height/2) ;
        
        self.calc_radii()
        ocircradius = self.trackRadius
        icircradius = self.wheelRadius
        holeradius = self.holeRadius
        inoutratio = 0
        x = 0
        xo = 0
        y = 0
        yo = 0
        holer = 0
        ocircr = 0
        icircr = 0
        oldx = 0
        oldy = 0
        icircum = 0
        ocircum = 0
        icircumaccum = 0
        ocircumaccum = 0
        icircrevs = 0
        ocircrevs = 0
        pi = 3.141592
        
        ocircr = (ocircradius-icircradius)
        icircr = icircradius
        holer = holeradius
        
        ocircum = pi*ocircradius*2
        icircum = pi*icircradius*2
        inoutratio = (icircradius / ocircradius)
        
        icircumaccum = icircum
        ocircumaccum = ocircum
        
        g.set_color(self.spiralColor)
        
        if(self.preview):
            self.hide_preview()
            
        while( int(icircumaccum) != int(ocircumaccum)):
            icircumaccum = icircumaccum + icircum
            icircrevs = icircrevs + 1
            
            if(icircumaccum>=ocircumaccum):
                ocircumaccum = ocircumaccum+ocircum
                ocircrevs = ocircrevs+1
            if(icircrevs == 100): 
                break
        
        oldx = (math.sin(0)*ocircr) + math.sin(0)*holer ;
        oldy = (math.cos(0)*ocircr) + math.cos(0)*holer ;
        
        i = 0
        spiralStep = pi / 180.0
        while(i <= 2*pi*(icircrevs+1)):
            xo = math.sin(i*inoutratio)*ocircr
            yo = math.cos(i*inoutratio)*ocircr
            x = xo + math.sin(-i)*holer
            y = yo + math.cos(-i)*holer
            g.draw_line(oldx, oldy, x, y)
            #g.draw_point(x, y)
            oldx = x 
            oldy = y
            i = i + spiralStep

    def set_pen_color(self, c):
        if(preview):
            hidePreview()
        
        if( c == "Black" ):
            penColor = Color.black
        elif( c == "Blue" ):
            penColor = Color.blue
        elif( c == "Cyan" ):
            penColor = Color.cyan
        elif( c == "DarkGray" ):
            penColor = Color.darkGray
        elif( c == "Green" ):
            penColor = Color.green
        elif( c == "LightGray" ):
            penColor = Color.lightGray
        elif( c == "Magenta" ):
            penColor = Color.magenta
        elif( c == "Orange" ):
            penColor = Color.orange
        elif( c == "Pink" ):
            penColor = Color.pink
        elif( c == "Red" ):
            penColor = Color.red
        elif( c == "White" ):
            penColor = Color.white
        elif( c == "Yellow" ):
            penColor = Color.yellow
        showPreview()

    def setHoleToWheel(self, r):
        if(preview):
            hidePreview()
        holeToWheel = r
        calcRadii()
        showPreview()

    def setWheelToTrack(self, r):
        if(preview):
            hidePreview()
        wheelToTrack = r
        calcRadii()
        showPreview()

    def setTrackToMax(self, r):
        if(preview):
            hidePreview()
        trackToMax = r
        calcRadii()
        showPreview()

    def paint(self, g):
        g.set_color(Color.white)
        #g.fill_rect(0,0,self.width,self.height)
        self.show_preview()
        
        
