1. License:

Copyright <2022>, <Anonymous160609>

Copying and distribution of this file, with or without modification, 
are permitted in any medium without royalty, 
provided the copyright notice and this notice are preserved. 
This file is offered as-is, without any warranty.


2. this ABM software:

It is an agent-based model simulating drunkens approaching homes from a pub. 
it has and simple interface-based configs. 
It simulates the movement of drunkens from a pub to their homes.
It process different drunken's leave, movement, and arrival of home one by one.
The movements of drunkens seperate into 2 methods: A proportion of conscious movement, 
based on average values bewteen their locations and their homes. A inconscious movement, 
based on random movement on 4 directions.
The arrival at home is defined as a Euclidian distance,
within a range it changes the coordinates of drunkens as their home coordinates.
The display of drunkens before arrival home is red, it changes to green after arrival at home.
The ABM also display all steps of all drunkens as white dots. 


3. Content:
|
|__model.py
|__agentframework.py
|__drunken.plan
|__steps_map.csv
|__README.txt
|__LICENSE.txt
|__Development Document.docx
|__old_version

model.py 
THE ONLY FILE TO BE USED BY USER.
it generates an UI for drunken-appraoching-home ABM display and parametre user-inputs.

agentframework.py 
is the module of the drunken agent class and its class methods of Move() and Step(), used in ABM.

drunken.plan 
a 2-D list of values ranging from 0 to 250, imported and used as the map in ABM.

steps_map.csv
An output of map from ABM, it stores drunkens' presences in locations as values of 3 in the map.
In other words, it changes from drunken.plan through the mulyiplication of 3s.

README.txt
This file, user manual.

LICENSE.txt
License of this ABM, regulating the use, modification and redistribution.

Development Document.docx
A detailed document explaining the development of this ABM and solutions to encountered issues.

old_version 
a folder of older versions of ABM component.


4. Operation:

This ABM software should run in anaconda through spyder, 
but users can try running though own measures, 
provded all required python environments. 
Open the model.py in spyder, it will show an interface. 
Input parametres then confirm then run through buttons.
Else, click "run" will initialize default parametres.
When running, it shows movements of drunkens from a pub to homes, one by one. 
the movement of drunkens is shown as red dots, while their steps are white dots.


5. Testing:

In 0.1 version:
These tests fix the basic running of the model.

	Wrong variable names:

		if ((agt.x - agt.homcntrd[1])**2 + (agt.y - agt.home[0])**2)**0.5 < 20 + 250/agt.alchohol:
		AttributeError: 'Drunken' object has no attribute 'homcntrd'
		FIX: homcntrd to homctrd

		if ((agt.x - agt.homctrd[1])**2 + (agt.y - agt.home[0])**2)**0.5 < 20 + 250/agt.alchohol:
		IndexError: list index out of range
		FIX: agt.home to agt.homctrd

		raise TypeError("Image data of dtype {} cannot be converted to "
		TypeError: Image data of dtype object cannot be converted to floaT
		FIX: matplotlib.pyplot.imshow(map) to matplotlib.pyplot.imshow(environment)


		if drunkens[i].x ==drukens[i].homctrd[1]:
		NameError: name 'drukens' is not defined
		FIX: drukens to drunkens

	Wrong data types:

		drunkens[num].homctrd[0] = homes[num][1]
		TypeError: 'tuple' object does not support item assignment
		FIX: homectrd data type from () to []


		self._y = (self._y + self.home._y)/2
		AttributeError: 'list' object has no attribute '_y'
		FIX: self.home._y to self.homctrd[0]

	Wrong module uses:

		if random(0,1) > self.alchohol/250:
		TypeError: 'module' object is not callable
		FIX: random(0,1) to to random.random

		if (self._y,self._x) in step:
		NameError: name 'step' is not defined
		FIX: step to self.step

		step.append([self._y,self._x])
		NameError: name 'step' is not defined
		FIX: step.append to self.step.append

In version 1.0:

	Fix wrong iteration bewteen drunkens:
	Put iterators into a call-back function to call in each ieration,
     	rather in the update()fucntion's scale, which will not accumulate 
	the iterator and pass to next iteration.

		Wrong:

		def update(frame_number):  
		...
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
		...

		Correct: 
		
		def Switch(agt):
    			global cqol
    			if agt.colour == 'Green':
        			cqol += 1
		
		......

		def update(frame_number):  
		...
		    for i in range(25):
				if int(i) == cqol:
            			Judge(drunkens[i])
           			 drunkens[i].Step()
            			drunkens[i].Move()
            			Switch(drunkens[i])
        	...

In version 1.1:
	
		Fix location mismatchments between drunkens and the map:
		In making drunken class instances, 
		exchange the inputs of x and y coordinates.

		Wrong:
		for num in range(len(drunkens)):
   			drunkens[num].alchohol = homes[num][0]
    			drunkens[num].homctrd[0] = homes[num][1]
    			drunkens[num].homctrd[1] = homes[num][2]

		Fix:
		for num in range(len(drunkens)):
   			drunkens[num].alchohol = homes[num][0]
			drunkens[num].homctrd[0] = homes[num][2]
    			drunkens[num].homctrd[1] = homes[num][1]
        
		
5. Issues:		

The display of this ABM are based on reverse axes.
Running effiency decreases with scatter steps increase.
the direct visualization of changes in map values is limited by matplotlib,
inobviouse else bleach over time.
the config of ABM is too simple.

6. Further Development: 

The display of this ABM are based on reverse axes, users are encourage to correct it 
through refactorizing the making of map from drunken.plan.

In obtaining better display of steps this ABM plots steps as scatter plots.
the running efficiency decreases with steps increase, users are encouraged
to increase the running efficiency.

The best display of steps is direct visualization of changes in map values.
However, small changes are difficult to identify in this appraoch,
it is the reason this ABM introduced scatter steps.
While big changes in map values will refactorize the map colours,
bleach the map due to the algorithm structure of matplotlib.
Users are encouraged to understand the running of matplotlib and avoid the temporal-serial 
refactorization of values and colours.

This ABM only has simple configs for users, users are encouraged to construct more configs,
based on the example in this ABM.

7. Reference:

read in .plan as list:
https://www.programiz.com/python-programming/reading-csv-files

turn text strings into numbers in reading .plan:
https://stackoverflow.com/questions/28376538/removing-quotation-marks-from-list-items

ABM framework and basic functions:
https://www.geog.leeds.ac.uk/courses/computing/study/core-python/



































