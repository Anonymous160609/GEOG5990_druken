# Author: Anonymous160609 (Github).
# Version: 


import tkinter 
import matplotlib 
matplotlib.use('TkAgg') 
import random  
import csv  
import time
import agentframework
import importlib  
importlib.reload(agentframework)  


cqol = 0

# 2. 
# https://www.programiz.com/python-programming/reading-csv-files
with open('drunk.plan', 'r') as file:
    reader = csv.reader(file)
    envirotrix = []
    for row in reader:
        row = [int(i) for i in row]
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
        row = [int(i) for i in row]
        environment.append(row)
        #print(row)
    del row
    del file
    del reader

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
    drunkens.append(agentframework.Drunken(pub[0],pub[1],environment,'Red'))
del num

for num in range(len(drunkens)):
    drunkens[num].alchohol = homes[num][0]
    drunkens[num].homctrd[0] = homes[num][1]
    drunkens[num].homctrd[1] = homes[num][2]
del num 


# random.seed(160609)
carry_on = True	
num_iterate = 500
def Judge(agt):
    # if ((agt.x - agt.homctrd[1])**2 + (agt.y - agt.homctrd[0])**2)**0.5 < 20 + 250/agt.alchohol:
    if ((agt.x - agt.homctrd[1])**2 + (agt.y - agt.homctrd[0])**2)**0.5 < 10:
        agt.y = agt.homctrd[0]
        agt.x = agt.homctrd[1]
        agt.colour = 'Green'
        # print("drunken:", agt.alchohol, "arrives at home")
    else:
        agt.y = agt.y
        agt.x = agt.x  
        
fig = matplotlib.pyplot.figure(figsize=(7, 7))
# def update(frame_number):  
#     """   

#     """
#     global drukens    
#     global carry_on
#     global stop_time
#     global num_iterate
#     global cqol

#     fig.clear()   
#     matplotlib.pyplot.xlim(0, 299)
#     matplotlib.pyplot.ylim(0, 299)
#     matplotlib.pyplot.imshow(environment) 
    

    
#     for i in range(25):
        
#         Judge(drunkens[i])
#         # drunkens[i].Step()
#         drunkens[i].Move()
        
#         for num in range(len(drunkens[i].step)):
#             matplotlib.pyplot.scatter(drunkens[i].step[num][0],drunkens[i].step[num][1],c='White')
#         # matplotlib.pyplot.scatter(drunkens[i].step[int(len(drunkens[i].step))-1][0],drunkens[i].step[int(len(drunkens[i].step))-1][1],c='White')             
#         matplotlib.pyplot.scatter(drunkens[i]._y,drunkens[i]._x,color=drunkens[i].colour)

def Switch(agt):
    global cqol
    if agt.colour == 'Green':
        cqol += 1
    
    
def update(frame_number):  
    """   

    """
    global drukens    
    global carry_on
    global stop_time
    global num_iterate
    global cqol

    fig.clear()   
    matplotlib.pyplot.xlim(0, 299)
    matplotlib.pyplot.ylim(0, 299)
    matplotlib.pyplot.imshow(environment) 
    
    
    for i in range(25):
        if int(i) == cqol:
            Judge(drunkens[i])
            drunkens[i].Step()
            drunkens[i].Move()
            Switch(drunkens[i])
        
            
            

                

                
    
    
    for i in range(25):
        

        
           
        matplotlib.pyplot.scatter(drunkens[i]._y,drunkens[i]._x,color=drunkens[i].colour)


def gen_function():
    a = 0
    global carry_on
    while (a < num_iterate) & (carry_on) :
        yield a
        a = a + 1
    if carry_on:
        print("Iteration number exceed, stop")

def Run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()  
    
 
root = tkinter.Tk()
root.title("ABM of wolf, sheep and consumings")
tkinter.Button(root,text="Run",command=Run).grid(row=11,column=0)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=0,rowspan=12,column=1) 
root.mainloop() 

with open('steps_map.csv', 'w') as file:

    write = csv.writer(file)
    write.writerows(environment)  

drunkens[24].step
