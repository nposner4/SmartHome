import readInJson


import datetime

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


def find_habits(data, ke, n_cluster):
	temp = []
	for key in ke:
		temp = data[(key, "accelx")]
	cluster = []
	for index, entry in temp.iterrows():
		cluster.append([entry[0], float(str(entry[1])[11:13])])
	data = temp
	kmeans = KMeans(n_clusters = n_cluster)
	
	kmeans.fit(cluster)
	labels = kmeans.predict(cluster)
	centers = kmeans.cluster_centers_
	
	z = [t[::-1] for t in centers]
	
	plt.scatter(*zip(*z))
	plt.title('Cluster centers')
	plt.xlabel('Time')
	plt.ylabel('Acceleration')
	plt.show()
	
	
		

