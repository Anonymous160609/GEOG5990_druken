"""
Drunken agent class of ABM
IMPORT AS MODULE ONLY
Author: Anonymous160609 (Github).
Version: 1.2. 
"""

import random # geenrate random numbers

class Drunken():
    """
    >>>drunken = Drunken(1,1, environment,colour)
    >>>drunken
    <agentframework.Drunken at ...>
    
    Class of drunkens in ABM
    
    Arguments:
    __init___: 4 essential parametres
    self.environment: shared map for drunkens to imteract
    self.colour: colours to display in animation
    self.step: previous locations of drunkens
    self.alchohol: serial number and alchohol intake of durnkens
    self.home: homes of drunkens to go
    self.homctrd: centroids of homes
    
    Returns:
    instances of class Drunken in ABM

    """
    def __init__ (self,_y,_x,environment,colour):
        """
        >>>drunken = Drunken(1,1,environment,colour)
        >>drunken.x
        1
        
        Essential parameters of drunkens
            
        Arguments:
        _y: y coordinate
        _x: x coordinate
        environment: 2-D list of a map
        colour: text string to display colour in animation, 'Color'
            
        Returns:
        instances of class Drunken        

        """
        #check in avoid no inputs
        if (_y == None):
            self._y = random.randint(138,158) #default value as pub's
        else:
            self._y =_y          
        if (_x == None):
            self._x = random.randint(128,148) #default value as pub's
        else:
            self._x =_x 

        self.environment = environment
        self.colour = colour
        #a nested list with 2 values, for appending and plotting
        self.step = [[self._y,self._x]]
        self.alchohol = 0 #drunken's number also alchohol intake
        self.home= [] #empty list for parametre passing
        self.homctrd = [0,0] # default centroids of drunken home

        
    def getx(self):
        """
        >>>drunken = agentframwork.Drunken(1,1,environment,colour)
        >>>drunken.getx
        <bound method Drunken.getx of <agentframework.Drunken object at ...>
        >>>drunken.x
        1
        
        For property() Method to encapsulate class values: _x.
        Display value of '_x' when call 'x'.
        
        returns:
        the value of _x when call x
        """
        
        return self._x

    def setx(self, value):
        """
        >>>drunken = agentframwork.Drunken(1,1,environment,colour)
        >>>drunken.setx(2)
        <bound method Drunken.getx of <agentframework.Drunken object at ...>
        >>>drunken.x
        2
        
        For property() Method to change encapsulated class values: _x.
        Change value of '_x' when call 'x'.
        
        returns:
        change the value of _y when call y
        """
        self._x = value
        
    x = property(getx, setx, "'x' property.")
    """
    link y to _y and its methods
    """
    
    def gety(self):
        """
        >>>drunken = agentframwork.Drunken(1,1,environment,colour)
        >>>drunken.gety
        <bound method Drunken.gety of <agentframework.Drunken object at ...>
        >>>drunken.y
        1
        
        For property() Method to encapsulate class values: _y.
        Display value of '_y' when call 'y'.
        
        returns:
        the value of _y when call y
        """
        return self._y

    def sety(self, value):
        """
        >>>drunken = agentframwork.Drunken(1,1,environment,colour)
        >>>drunken.sety(2)
        <bound method Drunken.gety of <agentframework.Drunken object at ...>
        >>>drunken.y
        2
        
        For property() Method to change encapsulated class values: _y.
        Change value of '_y' when call 'y'.
        
        returns:
        change the value of _y when call y
        """
        self._y = value
        
    y = property(gety, sety, "'y' property.")
    """
    link y to _y and its methods
    """
    
    #changed to function in model.py, for potential parameter setting by users
    # def Judge(self):
    #     if ((self._x - self.homcntrd[1])**2 + (self._y - self.home[0])**2)**0.5 < 20 + 250/self.alchohol:
    #         self._y = self.homcntrd[0]
    #         self._x = self.homcntrd[1]
    #     else:
    #         self._y = self._y
    #         self._x = self._x  
            
    def Move(self):
        """
        >>>drunken = Drunken(1,1,environment,colour)
        >>>a = drunken.x
        >>>drunken.Move
        >>>b = drunken.x
        >>>a == b
        False
        
        Move drunken 
        
        Arguements:
        step: list storing previous coordinates
        _y: y coordinate of drunken
        _x: x coordinate of drunken
        
        Returns:
        record current coordinates,
        changes in drunkens coordinates,
        2 potential movements of conscious or not
        in general getting close to homes        

        """
        
        #cut front coordinates if the length excesses 50 
        if len(self.step) > 20:
            for i in range(len(self.step)-50):
                del self.step[i]
        #check drunken is not at home, thus move and save memory        
        if ((self._y != self.homctrd[0])&(self._x != self.homctrd[1])):
            #check drunken is not at pub, thus move and save memory
            if ((self._y != self.step[0][0]) & (self._x != self.step[0][1])):
                #record current coordinates
                self.step.append([self._y,self._x])
            else:
                self.step = self.step
             #conscious move, based on alchohol intake
            if random.random() > (self.alchohol/250 - 0.05):
                # self._y = (self._y + self.homctrd[0])/2
                # self._x = (self._x + self.homctrd[1])/2
                #introduced a cache 
                #move drunkens to home more gradually, less 'teleport'
                homerom_y = (self._y + self.homctrd[0])/2 + random.randint(-10,10)
                homerom_x = (self._x + self.homctrd[1])/2 + random.randint(-10,10)
                self._y = (self._y + homerom_y)/2
                self._x = (self._x + homerom_x)/2
            #inconscious move
            else:
                #introduced a cache,
                #for drunken steps check 
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
        #if in home or pub, stay still
        else:
            self._y = self._y 
            self._x = self._x
    
    def Step(self):
        """
        >>>enviro = [[1]]
        >>>drunken = Drunken(0,0,enviro,colour)
        >>>drunekn.Move
        >>>enviro
        4
        
        Store all drunkens's stay in any locations on map
        
        Arguements:
        environment: 2-D list
        
        Returns:
        changes in list values
        """
        self.environment[int(self._y)][int(self._x)] += 3
                