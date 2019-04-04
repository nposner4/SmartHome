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
	numHome = "ALL"  # Use everything is 'ALL'; otherwise integer
	numModality = [0,1,2]
	showPLOT = True
	isNORMALIZED = True
	startDate = datetime.date(2017, 9, 11)
	endDate = datetime.date(2017, 9, 12)
	for key in objects.keys():
		if feature in objects[key]:
			door[key] = objects[key]
	return door
			

def do_cluster(data, ke, n_cluster):
    temp = []
    for key in ke:
        temp = data[(key, "accelx")]
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
    sort_center = [t[::-1] for t in centers]
    print(sort_center)
    threshold = 0
    l = list(map(lambda x: x[0], sort_center))
    l.sort()
    for i in range(len(l) - 1):
        if abs(l[i+1] - l[i]) > threshold:
            threshold = abs(l[i+1] - l[i])
    print(threshold)            
    x = []
    y = []
    for point in cluster:
        x.append(point[1])
        y.append(point[0])
        min_d = 50
        for c in l:
            if abs(point[1] - c) < min_d:
                min_d = abs(point[1] - c)
        if min_d > threshold:
            print("ANOMALY FOUND " + str(point[1]))
		
	# Create plot
	#~ fig = plt.figure()	
    plt.scatter(x,y)
    plt.title('Door')
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.show()

			

def day_of_time(timeframe):
	 pass
				
			
			
		
	
	
