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


# Finds the object we are looking for in the house and returns the feature.
def find_feature(objects, feature):
	door = {}
	dataDir = '/field/'
	fileName = "*.json"
	numHome = "ALL" 
	numModality = [0,1,2]
	showPLOT = True
	isNORMALIZED = True
	startDate = datetime.date(2017, 9, 11)
	endDate = datetime.date(2017, 9, 12)
	for key in objects.keys():
		if feature in objects[key]:
			door[key] = objects[key]
	return door
			

# Does the clustering and plots it in the end
def do_cluster(data, ke, n_cluster):
    temp = []
    for key in ke:
        temp = data[(key, "accelx")]
        print(temp)
    cluster = []
    for index, entry in temp.iterrows():
        cluster.append([entry[0], float(str(entry[1])[11:13] + "." + str(entry[1])[14:16])])
    data = temp
    kmeans = KMeans(n_clusters = n_cluster)
    kmeans.fit(cluster)
    labels = kmeans.predict(cluster)
    centers = kmeans.cluster_centers_
    # Swap entries in tuples for plotting
    sort_center = [t[::-1] for t in centers]
    
    # Get threshold for the biggest distance between neighbouring centers
    threshold = 0
    l = list(map(lambda x: x[0], sort_center))
    l.sort()
    for i in range(len(l) - 1):
        if abs(l[i+1] - l[i]) / 2 > threshold:
            threshold = abs(l[i+1] - l[i]) / 2          
    x = []
    y = []
    x_anomaly = []
    y_anomaly = []
    
    # Get all the datapoints and spot the anomalies. An anomaly is defined by a data point
    # that is further removed from a center than the biggest distance between two neighbouring centers
    for point in cluster:
        min_d = 50
        for c in l:
            if abs(point[1] - c) < min_d:
                min_d = abs(point[1] - c)
        if min_d > threshold:
            x_anomaly.append(point[1])
            y_anomaly.append(point[0])
            print("ANOMALY FOUND ON TIME: " + str(point[1]))
        else:
            x.append(point[1])
            y.append(point[0])
		
	# Create plot
    plt.close("all")
    fig = plt.figure()
    ax1 = fig.add_subplot(111)	
    ax1.scatter(x,y, c= 'g', label = "data points")
    ax1.scatter(x_anomaly, y_anomaly, c='r', label = "anomily")
    plt.title('Clustering')
    plt.xlabel('Time')
    plt.ylabel('Acceleration')
    plt.legend(loc = "upper left")
    plt.show()


			
			
		
	
	
