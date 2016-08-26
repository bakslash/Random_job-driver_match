"""
Given 50 randomly located drivers, map them to some random number of randomly located jobs such that
total distance to jobs is minimised. 

1. What's the complexity of your algorithm with respect to the number of iterations?
2. How many drivers will be at each location at the end of 1000 iterations?*
3. How many turns will an average customer have to wait after 200 iterations?
4. How many excess jobs should we expect after 300 iterations?
5. On average, how far is a driver from a customer? What if there were only 5 drivers?
6. If locations 1-5 had 1-100 jobs and locations 6-10 had 1-10 jobs , what would the answers to 2-5 above be?
7. Given the situation in question 6 and given only 5 drivers, does your algorithm still work? If not how do you fix it?

Your code is meant to locally and globally optimise matching, the job number is between 1 and 100, 
and should update driver location and loop for at least 10 iterations. 

"""


"""

This snippet will efficiently work with a specified number of job ids whereby each location is treated as a 
location id. I.e. while running on an app, the job locations available as by customer needs will be used to
compute their distances to the closest driver, also given the number of drivers.



driver range = 50
job number = randomly located(generated) for mapping in range 1 - 100
Pseudocode:

first loops through all the driver ids.
A new list is created for all the driver ids where they are stored
Then Generates a random job location id in the range 1-100 for the 50 drivers.
The job location ids are stored in another seperate list
Checks whether the  driver ids and random job locations are in range
A dictionary is then created to map each driver to the closest location and 
finally printed out to the console.

"""

from random import randint




for id in range(1,50):
	id_list = []
	id_list.append(id)
	# updating id_list
	#print id_list
	j_location = randint(1,100)
	location_list = []
	location_list.append(j_location)
	#update location_list
	# print location_list
	if id >= j_location <= 100:
			# item_list.append(id)
			# print item_list
		list = dict(zip(id_list, location_list))
		print list
		# This list cotains all the drivers and locations closest to each other





