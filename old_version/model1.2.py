"""
ABM of durnkens appraoching homes.
THIS IS THE FILE EXPECTED TO BE USED BY USERS.
Author: Anonymous160609 (Github).
Version: 1.2.
"""

#1.
#Script Environments
import tkinter #intewrface 
import matplotlib #animation
matplotlib.use('TkAgg') 
import csv #file read-in/out for ABM environmnet 
import time #timing for ABM running
import agentframework #class Drunken in ABM
import importlib #reload agentframework after adjust
importlib.reload(agentframework) #reload agentframework after adjust 

#2.
#Set up variables 

#2.1.
#read in ABM environment as a list
# https://www.programiz.com/python-programming/reading-csv-files
with open('drunk.plan', 'r') as file:
    reader = csv.reader(file) 
    envirotrix = [] #empty list for homes
    for row in reader:
        # https://stackoverflow.com/questions/28376538/removing-quotation-marks-from-list-items
        row = [int(i) for i in row] #clange text '' to number
        envirotrix.append(row)
        #print(row)
    del row, file, reader #dismiss useless variables

for i in range(300): #each row
    for j in range(300): # each column
        #mutate envirotrix to (value, y coordinate, xcoordinate)
        envirotrix[i][j] = (envirotrix[i][j],int(i),int(j))
        
#make environment image in ABM animation display 
with open('drunk.plan', 'r') as file:
    reader = csv.reader(file)
    environment = []
    for row in reader:
        row = [int(i) for i in row]
        environment.append(row)
        #print(row)
    del row, file, reader

#print(map[22][22])
# house 250 (y,x): (22,21) (32, 31)
#for i in range(299):
    #for j in range(299):
        #if map[i][j] == 250:
            #print(i,j)
#2.2.
#locate the pub
for i in range(300):
    for j in range(300):
        a = [] #all values meet the pub feature
        if environment[i][j] == 1: #if values in environment is that of pub
            a.append((int(i),int(j))) #make a 2-D list of pub rasters
            y = 0
            x = 0
            for i in range(len(a)):
                    y += a[i][0]
                    x += a[i][1]                    
                    pub = ((y/len(a)),x/len(a)) #pub coordinates from averges
del y,x,a,i,j

#2.3.
#make homes from envirotrix
homes = [] # (alchohol,y,x)
for k in range(1,26,1): #natural number [1,25]
    a = []
    for i in range (300):
        for j in range(300):
            #if environment values are alchohols
            if  envirotrix[i][j][0] == 10*k: 
                y = 0
                x = 0
                a.append((int(i),int(j)))
                for l in range(len(a)):
                    y += a[l][0]
                    x += a[l][1]         
    homes.append((k*10,y/len(a),x/len(a)))
del k,a,j,l,i,x,y

#2.4.                
#make drunkens instances from Drunken class, with values from environment
drunkens = []
for num in range(len(homes)):
    #initials: 
    #location of drunkens: in pub
    #environment: envirtonment varaiable, the map
    #colour: red
    drunkens.append(agentframework.Drunken(pub[0],pub[1],environment,'Red'))
del num

#2.5.
#locate drunkens' homes based on their features 
for num in range(len(drunkens)):
    drunkens[num].alchohol = homes[num][0]
    """
    the display of image is adjusted to reverse axes, to match drunken plotting 
    """
    # drunkens[num].homctrd[0] = homes[num][1]
    # drunkens[num].homctrd[1] = homes[num][2]
    drunkens[num].homctrd[0] = homes[num][2]
    drunkens[num].homctrd[1] = homes[num][1]
del num 

#2.6.
#make ABM parameters
# random.seed(160609)
cqol = 0 #sequence to move drunkens one by one
carry_on = True	#if to contibue the ABM in each iteration
num_iterate = 200 #maximal number of ABM iterations
start_time = 0.0     
stop_time = 0.0

#3.
#functions

#3.1.
#ABM agent movement functions
def Judge(agt):
    """
    >>>drunken = agentframework.Drunken(1,1,environment,colour)
    >>>drunekn.homectrd = [0,0]
    >>>Judge(drunken)
    >>>(drunken.y,drunekn.y)
    (0,0)
    
    Function for dunkens to identify the distance to home, 
    if in radius make them move to home, else stay location.
    
    Arguements:
    agt: class instance Drunken
    agt.x: x coordinate
    agt.y: y coordinate
    agt.homctrd: list, 2 unit length, hoctrd[0] and homctrd[1] are centroid 
    coordinates of drunken's home
    """
    if ((agt.x - agt.homctrd[1])**2 + (agt.y - agt.homctrd[0])**2)**0.5 < 20 + 250/agt.alchohol:
    # if ((agt.x - agt.homctrd[1])**2 + (agt.y - agt.homctrd[0])**2)**0.5 < 10:
        agt.y = agt.homctrd[0]
        agt.x = agt.homctrd[1]
        agt.colour = 'Green' #change at-home drunkens to green
        # print("drunken:", agt.alchohol, "arrives at home")
    else:
        agt.y = agt.y
        agt.x = agt.x  
        
def Switch(agt):
    """
    >>>cqol = 0
    >>>drunken = agentframework.Drunken(1,1,environment,'Green')
    >>>Switch(drunken)
    >>>cqol
    1
    
    Function to move drunkens one by one, 
    and stop ABM after all drunkens arrive home.
    
    Arguements:
    cqol: global varaible of processing sequence
    agt.colour: the colour text of class Drunken
    
    Returns:
    accumulating cqol, for Update() function to match 
    """
    global cqol
    global carry_on
    global start_time
    global stop_time
    if agt.colour == 'Green':
        cqol += 1
    if cqol == 25:
        carry_on = False
        stop_time = time.process_time()
        print('All drunkens arrive homes')
        print("Excuting time:",(stop_time - start_time))

#3.2.
#animation functions 
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #instance of animation in interface
def update(frame_number):  
    """   
    2 lists of interactions and animations of drunkens:
        
    I.I. judge distance to home
    I.II. store current locations into map
    I.III. drunkens move homes
    I.IV. if current drunken gets home, move next drunken
    
    II.I plot all steps of drunkens as white scatter dots
    II.II plot all drunkens in moving or in staying
    
    Keyword argument:
    fame_number -- each frame (ABM iteration) in animation in tkiner for ABM
      
    Returns:
    Changes of ABM reflected as an animation

    """
    #call variables to use
    global drukens
    global num_iterate
    global cqol
    

    fig.clear() #clean image from last run  
    matplotlib.pyplot.xlim(0, 300) #size of image
    matplotlib.pyplot.ylim(0, 300)
    matplotlib.pyplot.imshow(environment) #show ABM environment
    
    #packaged ABM agent activitiy functions
    for i in range(25):
        #move drunkens one by one
        if int(i) == cqol:
            Judge(drunkens[i])
            drunkens[i].Step()
            drunkens[i].Move()
            Switch(drunkens[i])
            
    #packaged ABM animation function    
    for i in range(25):
        for num in range(len(drunkens[i].step)):
            matplotlib.pyplot.scatter(drunkens[i].step[num][0],drunkens[i].step[num][1],c='White')
        #test plotting, only one previous location
        # matplotlib.pyplot.scatter(drunkens[i].step[int(len(drunkens[i].step))-1][0],drunkens[i].step[int(len(drunkens[i].step))-1][1],c='White')             
        matplotlib.pyplot.scatter(drunkens[i]._y,drunkens[i]._x,color=drunkens[i].colour)

#informatic fucntion in ABM running
def gen_function():
    """
    Informative function of ABM stopping causes.

    Arguments:
    a: local iterator, to count number of ietraions
    num_iterate: passed global parameter deciding required run times of ABM
    
    
    Returns:
    Once iteration number exceeds,
    print text.
    """
    a = 0
    global carry_on
    global start_time
    global stop_time

    
    while ((a < num_iterate) & (carry_on)):
        yield a
        a = a + 1
    if carry_on:
        stop_time = time.process_time()
        print("Iteration number exceed, stop")
        print("Excuting time:",(stop_time - start_time))
#3.3.
#interface config functions        
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
    global num_iterate
    global start_time  # for timing the code
    start_time = time.process_time()  # to subtract in monitor in tkinter
    
    global num_of_agents  # for parameter passing
    if buttom_iteratnnum.get():
        if int(buttom_iteratnnum.get())  <= 0:
            print("wrong value, set to initail vlaue")
            num_iterate = 200
        elif int(buttom_iteratnnum.get())  >= 400:
            print("rnning time too lang, set to initail vlaue")
            num_iterate = 200
        else:
            print("Iteration number pass succeed")
            num_iterate = int(buttom_iteratnnum.get()) 
    else:
        print("No iteration number input, set to initial value")
        num_iterate = 200

#onclikck function to initiate ABM
def Run():
    """
    On-click function to initialize ABM 
    
    Arguements:
    animation: matplotlib FuncAnimation made of previous created fig, update(),
    and gen_function(), i.e. the instance of ABM animation
    canvas: the container for the animation
    
    Returns:
    a running ABM
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()  #draw ABM in tkinter
    
#4.
#ABM interface
root = tkinter.Tk() #general interface structure
root.title("ABM of drunkens from the pub to homes")
tkinter.Label(root,text="Iteration Number: (0,400]").grid(row=2,column=0)
buttom_iteratnnum = tkinter.Entry(root)
buttom_iteratnnum.grid(row=3,column=0)
tkinter.Button(root,text="Confirm", command=confirm).grid(row=10,column=0)
tkinter.Button(root,text="Run",command=Run).grid(row=11,column=0)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.grid(row=0,rowspan=12,column=1) 
root.mainloop() 


#5.
#output ABM results in environment as file
#save interacted ABM environment as a csv file 
with open('steps_map.csv', 'w') as file:
    # using csv.writer method from CSV package
    write = csv.writer(file)
    write.writerows(environment)  

# for i in range(300):
#     for j in range(300):
#         if environment[i][j] == 3:
#             print((int(i),int(j)))