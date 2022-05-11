
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


# 2. 
# https://www.programiz.com/python-programming/reading-csv-files
with open('drunk.plan', 'r') as file:
    reader = csv.reader(file)
    envirotrix = []
    for row in reader:
        # https://stackoverflow.com/questions/28376538/removing-quotation-marks-from-list-items
        # row = [int(i) for i in row]
        row = [float(i) for i in row]
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
    drunkens.append(agentframework.Drunken(pub[0],pub[1],environment,'White'))
del num

for num in range(len(drunkens)):
    drunkens[num].alchohol = homes[num][0]
    drunkens[num].homctrd[0] = homes[num][1]
    drunkens[num].homctrd[1] = homes[num][2]
del num 

num_iterate = 500


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
    

            
                

def Judge(agt):
    if ((agt.x - agt.homctrd[1])**2 + (agt.y - agt.homctrd[0])**2)**0.5 < 20 + 250/agt.alchohol:
        agt.y = agt.homctrd[0]
        agt.x = agt.homctrd[1]
    else:
        agt.y = agt.y
        agt.x = agt.x  
        

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

        if drunkens[i].y ==drunkens[i].homctrd[0]: 
            if drunkens[i].x ==drunkens[i].homctrd[1]:
                cqol += 1
            else: cqol = cqol
        else:
            cqol = cqol
            

        Judge(drunkens[cqol])

        drunkens[cqol].Move()  
        iterate += 1
        if iterate > num_iterate:
            drunkens[cqol].y ==drukens[cqol].homctrd[0]
            drunkens[cqol].x ==drukens[cqol].homctrd[1]
        if cqol == 24:
            carry_on = False
            

    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment)

    for i in range(25):
        matplotlib.pyplot.scatter(drunkens[i]._y,drunkens[i]._x,color=drunkens[i].colour)

    stop_time = time.process_time()
        
  
def gen_function():
    """

    """
    a = 0 
    global carry_on

    while (a < num_iterate) & (carry_on) :

        yield a
        a = a + 1

    if carry_on:
        print("Iteration number exceed, stop")
        print("Excuting time:", (stop_time-start_time))

 
def Run():
    """ 

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)

    canvas.draw()  

   
# 5.3.
# Parameter input function.

def confirm ():
    """
  
    """
    global start_time 
    start_time = time.process_time()  



  
root = tkinter.Tk() 
root.title("ABM of wolf, sheep and consumings")





tkinter.Button(root,text="Run",command=Run).grid(row=11,column=0)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)

canvas._tkcanvas.grid(row=0,rowspan=12,column=1) 




root.mainloop() 


with open('steps_map.csv', 'w') as f:

    write = csv.writer(f)
    write.writerows(environment)
