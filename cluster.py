import readInJson

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd
import datetime
from sklearn.cluster import KMeans
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
matplotlib.style.use('ggplot')



def find_feature(objects, feature):
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
		if feature in objects[key]:
			door[key] = objects[key]
	return door
			

def do_cluster(data, ke, n_cluster):
	temp = []
	for key in ke:
		temp = data[(key, "accelx")]
		print("quick brown fox")
		print(temp)
	cluster = []
	for index, entry in temp.iterrows():
		cluster.append([entry[0], float(str(entry[1])[11:13])])
	#temp["timestamp"].map(lambda x:0)
	data = temp
	print(cluster)
	kmeans = KMeans(n_clusters = n_cluster)
	
	kmeans.fit(cluster)
	labels = kmeans.predict(cluster)
	centers = kmeans.cluster_centers_
	x = []
	y = []
	for point in cluster:
		x.append(point[1])
		y.append(point[0])
		
	# Create plot
	fig = plt.figure()	
	plt.scatter(x,y)
	plt.title('Door')
	plt.xlabel('Time')
	plt.ylabel('Acceleration')
	plt.show()

			

def day_of_time(timeframe):
	 pass
				
			
			
		
	
	
