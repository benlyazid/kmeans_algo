import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math
import copy

COLORS = ['red', 'blue', 'green']

#		Calcule the destance
def destance_2_points(p0, p1):
	dx = (p0[0] - p1[0])**2
	dy = (p0[1] - p1[1])**2
	return math.sqrt(dx + dy)

#		Update the center of K_points by calculing the average of each points
def update_center_of_k_points(data_lst, k_center):
	new_points = []
	for i in range(len(data_lst)):
		center = data_lst[i]
		average_a, average_b = 0, 0
		j = 0
		for _ in range(len(center)):
			values = center[j]
			v_a = values[0]
			v_b = values[1]
			average_a += v_a
			average_b += v_b
			j += 1
		average_a /= j
		average_b /= j	
		new_points.append([average_a, average_b])
	i  = 0  
	for _, k_point in k_center.iterrows():
		k_point['a'] = new_points[i][0]
		k_point['b'] = new_points[i][1]
		i += 1
	return k_center

#		Find The closest center to the point by calculing the destance
def get_the_closest_center(av, bv):
	global k_center
	min_dest = -1
	result_index = 0
	i = 0
	for index, center in k_center.iterrows():
		a_center = center['a']
		b_center = center['b']
		a_dest = pow(a_center - av, 2)
		b_dest = pow(b_center - bv, 2)
		dest =  math.sqrt(a_dest + b_dest)
		if min_dest == -1 or min_dest > dest:
			min_dest = dest
			result_index = i	
		i += 1	
	return result_index

#		Assign points to the closest cluster Points centroid and put it in the list by k index
def assign_points_to_the_closeest_center():
	global k_center, data, K
	data_lst = [[] for _ in range(K)]
	for index, row in data.iterrows():
		av = row['a']
		bv = row['b']
		close_one = get_the_closest_center(av, bv)
		data_lst[close_one].append([av, bv])
	k_center = update_center_of_k_points(data_lst, k_center)
	return data_lst

#		Calcule The defferent between the old k_point and the new after the update 
def average_of_changing(old):
	global k_center
	old_value = []
	new_value = []
	dest = 0
	for  _, v in old.iterrows():
		old_value.append([v['a'],v['b']])
	for _, v in k_center.iterrows():
		new_value.append([v['a'],v['b']])
	for i in range(len(old_value)):
		dest += destance_2_points(old_value[i], new_value[i])
	return dest


data =  pd.read_csv('simpleData.csv')
K = 3
k_center = data.sample(n=K)
reapet = 0
old = copy.copy(k_center)
change = 0

#		Reapet the K_mean algo Untel the defferent between the old points and the new == 0
while reapet == 0 or change != 0:
	old = copy.copy(k_center)
	reapet += 1
	data_lst = assign_points_to_the_closeest_center()
	change = average_of_changing(old)

#		Show the Data
for i in range(len(data_lst)):
	data = data_lst[i]
	for j in range(len(data)):
		plt.scatter(data[j][0], data[j][1], c=COLORS[i])

plt.xlabel("a_Values")
plt.ylabel('b_Values')
plt.show()
