

# Author: Anonymous160609 (Github).
# Version: 

import random 

class Drunken():
    """

    """
    def __init__ (self,_y,_x,environment,colour):
        """

        """
        
        if (_y == None):
            self._y = random.randint(138,158)
        else:
            self._y =_y          
        if (_x == None):
            self._x = random.randint(128,148)
        else:
            self._x =_x 

        self.map = map
        self.colour = colour
        self.step = []
        self.alchohol = 0
        self.home= [] 
        self.homctrd = (0,0)

        
    def getx(self):
        """

        """
        
        return self._x

    def setx(self, value):
        """

        """
        self._x = value
        
    x = property(getx, setx, "I am the 'x' property.")

    def gety(self):
        """

        """
        return self._y

    def sety(self, value):
        """

        """
        
        self._y = value
        
    y = property(gety, sety, "I am the 'y' property.")
    
    def Judge(self):
        if ((self._x - self.homcntrd[1])**2 + (self._y - self.home[0])**2)**0.5 < 20 + 250/self.alchohol:
            self._y = self.homcntrd[0]
            self._x = self.homcntrd[1]
        else:
            self._y = self._y
            self._x = self._x  
            
    def Move(self):
        """

        """
        global Judge
        global step

        step.append((self._y,self._x))

        if random(0,1) > self.alchohol/250:
            self._y = (self._y + self.home._y)/2
            self._x = (self._x + self.home._x)/2
        else:
            romy = self._y + random.randint(-10,10)
            romx = self._x + random.randint(-10,10) 
            self._y = self._y + random.randint(-10,10)
            self._x = self._x + random.randint(-10,10) 
            if (self._y,self._x) in step:
                self._y = self._y
                self._x = self._x
            else:
                self._y = romy
                self._x = romx
    
    def Step(self):
        """
        """
        self.environment[self._y][self._x] += 2
                