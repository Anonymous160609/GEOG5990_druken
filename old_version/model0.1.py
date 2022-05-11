
# Author: Anonymous160609 (Github).
# Version: 

import tkinter  

import matplotlib   
matplotlib.use('TkAgg') 
import random  

import operator
import csv  
import time
import agentframework
import importlib
importlib.reload(agentframework) 



with open('drunk.plan', 'r') as file:
    reader = csv.reader(file)
    envirotrix = []
    for row in reader:

        row = [int(i) for i in row]
        #map.append(row)
        envirotrix.append(row)
        #print(row)
    del row
    del file
    del reader
for i in range(300):
    for j in range(300):
        envirotrix[i][j] = (envirotrix[i][j],int(i),int(j))
        
with open('drunk.plan', 'r') as file:
    reader = csv.reader(file)
    environment = []
    for row in reader:
        # https://stackoverflow.com/questions/28376538/removing-quotation-marks-from-list-items
        row = [int(i) for i in row]
        environment.append(row)
        #print(row)
    del row
    del file
    del reader

#print(map[22][22])
            
# house 250 (y,x): (22,21) (32, 31)
#for i in range(299):
    #for j in range(299):
        #if map[i][j] == 250:
            #print(i,j)

                   


for i in range(300):
    for j in range(300):
        a = []
        if environment[i][j] == 1:
            a.append((int(i),int(j)))
            y = 0
            x = 0
            for i in range(len(a)):
                    y += a[i][0]
                    x += a[i][1]                    
                    pub = ((y/len(a)),x/len(a))
del y,x,a,i,j

homes = []
for k in range(1,26,1):
    a = []
    for i in range (300):
        for j in range(300):
            if  envirotrix[i][j][0] == 10*k:
                y = 0
                x = 0
                a.append((int(i),int(j)))
                for l in range(len(a)):
                    y += a[l][0]
                    x += a[l][1]         
    homes.append((k*10,y/len(a),x/len(a)))
del k,a,j,l,i,x,y
                

drunkens = []
for num in range(len(homes)):
    drunkens.append(agentframework.Drunken(pub[0],pub[1],map,'White'))
del num

for num in range(len(drunkens)):
    drunkens[num].alchohol = homes[num][0]
    drunkens[num].homctrd[0] = homes[num][1]
    drunkens[num].homctrd[1] = homes[num][2]
del num 

num_iterate = 50


random.seed(160609)

carry_on = True	

start_time = 0.0     
stop_time = 0.0

 
fig = matplotlib.pyplot.figure(figsize=(7, 7))

ax = fig.add_axes([0, 0, 1, 1])  


steps = list()
steps = [0]*300
for i in range(300):
    steps[i] = [0] * 300
    
for num in range(len(drunkens)):
    for lng in range(len(drunkens[num].step)):
        map[drunkens[num].step[0]][drunkens[num].step[1]] += 1
            
                


        

def update(frame_number):  
    global drukens
    """   

    """
    

    fig.clear()   
    

    global carry_on
    global stop_time
    global num_iterate

    

    for i in range(25):
        cqol = 0
        iterate = 0
        if drunkens[i].y ==drukens[i].homctrd[0]:   
            if drunkens[i].x ==drukens[i].homctrd[1]:
                cqol += 1
            else: cqol = cqol
        else:
            cqol = cqol
            
        drunkens[cqol].Judge()   
        drunkens[cqol].Move() 
        iterate += 1
        if iterate > num_iterate:
            drunkens[cqol].y ==drukens[cqol].homctrd[0]
            drunkens[cqol].x ==drukens[cqol].homctrd[1]
        if cqol == 24:
            carry_on = False
            

    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(map)


    for i in range(25):
        matplotlib.pyplot.scatter(drunkens[i]._y,drunkens[i]._x,color=drunkens[i].colour)
    

    stop_time = time.process_time()
        
   
def gen_function():
    """

    """
    a = 0 

    global carry_on

    while (a < num_of_iterations) & (carry_on) :

        yield a
        a = a + 1

    if carry_on:
        print("Iteration number exceed, stop")
        print("Excuting time:", (stop_time-start_time))


def run():
    """ 
    On-click function to triggle ABM's running (then stopping).     

    Arguments: 
    animation: Make this ABM an istance based on previous functions in section 5.,
    and based on FuncAnimation method of matplotlib package, to display 
    changes in each iteration. Its sub-arguments: fig, update, 
    frames=gen_function, repeat=False (explianed in previous documentations, 
    also see documentation of matplotlib.animation.FuncAnimation)
    canvas.draw(): draw animation instacne on the graphic weidge of tkinter
    
    Returns: 
    display this ABM as graphics in tkinter
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

    canvas.draw() 

   


def confirm ():
    """
    On-click function to pass parameters from user inputs in tkinter UI to ABM.
    It also detects and changes error-causing parameters to appropriate values.
    
    Arguments:
    button_sheepnum.get(): get value from tkinter entry of sheep number parameter
    buttom_iterationnum.get(): get value from tkinter entry of iteration number 
    parameter
    button_random.get(): get value from tkinter entry of stopping chance in
    each iteration
    button_neighbournum.get(): get value from tkinter entry of sheep's radious 
    for sharing grass
    button_preyredious.get(): get value from tkinter entry of wolf's radious of 
    preying sheep
    
        
    Returns: 
    number_of_sheep = button_sheepnum.get(), in 3.1.
    number_of_iterations = buttom_iterationnum.get(), in 3.1.
    random.radom() < button_random.get(), in update() in 5.1.
    neighbourhood = button_neighbournum.get(), in 3.3.
    (((a._x - b._x)**2) + ((a._y - b._y)**2))**0.5 < button_preyredious.get(),
    in prey() in 5.1.
    
    """
    global start_time  
    start_time = time.process_time()  




root = tkinter.Tk() 
root.title("ABM of wolf, sheep and consumings")





canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

canvas._tkcanvas.grid(row=0,rowspan=12,column=1) 

 
root.mainloop() 


with open('steps_map.csv', 'w') as f:

    write = csv.writer(f)
    write.writerows(map)
