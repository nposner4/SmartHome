import readInJson


import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import datetime
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
matplotlib.style.use('ggplot')



def findDoor(objects):
	door = {}
	dataDir = '/field/'  #'/data/'
	fileName = "*.json"
	numHome = 2  # Use everything is 'ALL'; otherwise integer
	numModality = [0,1,2]
	showPLOT = True
	isNORMALIZED = True
	startDate = datetime.date(2017, 9, 1)
	endDate = datetime.date(2017, 9, 29)
    
	for key in objects.keys():
		if "Door" in objects[key]:
			door[key] = objects[key]
			print(door[key])
			
			
		
			
			
			
			
		
	
	
