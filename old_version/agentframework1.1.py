

# Author: Anonymous160609 (Github).
# Version: 

import random # geenrate random numbers

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

        self.environment = environment
        self.colour = colour
        self.step = [[self._y,self._x]]
        self.alchohol = 0
        self.home= [] 
        self.homctrd = [0,0]

        
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
    
    # def Judge(self):
    #     if ((self._x - self.homcntrd[1])**2 + (self._y - self.home[0])**2)**0.5 < 20 + 250/self.alchohol:
    #         self._y = self.homcntrd[0]
    #         self._x = self.homcntrd[1]
    #     else:
    #         self._y = self._y
    #         self._x = self._x  
            
    def Move(self):
        """

        """
        if len(self.step) > 50:
            for i in range(len(self.step)-50):
                del self.step[i]
                
        if ((self._y != self.homctrd[0])&(self._x != self.homctrd[1])):
            if ((self._y != self.step[0][0]) & (self._x != self.step[0][1])):
                self.step.append([self._y,self._x])
            else:
                self.step = self.step
            if random.random() > (self.alchohol/250 - 0.05):
                # self._y = (self._y + self.homctrd[0])/2
                # self._x = (self._x + self.homctrd[1])/2
                homerom_y = (self._y + self.homctrd[0])/2 + random.randint(-10,10)
                homerom_x = (self._x + self.homctrd[1])/2 + random.randint(-10,10)
                self._y = (self._y + homerom_y)/2
                self._x = (self._x + homerom_x)/2
            else:
                # self.step.append([self._y,self._x])
                yrom = self._y + random.randint(-2,2)
                xrom = self._x + random.randint(-2,2) 
                if [yrom,xrom] in self.step:
                    print("don't get back")
                    self._y = self._y
                    self._x = self._x
                else:
                    self._y = yrom
                    self._x = xrom
        else:
            self._y = self._y 
            self._x = self._x
    
    def Step(self):
        """
        """
        self.environment[int(self._y)][int(self._x)] += 3
                