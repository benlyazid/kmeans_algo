import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import math


def get_the_closest_center(av, bv, centers):
	min_dest = -1
	result_index = 0
	i = 0
	for index, center in centers.iterrows():
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


def assign_points_to_the_closeest_center():
	global k_center, data, K
	data_lst = [[] for _ in range(K)]
	for index, row in data.iterrows():
		av = row['a']
		bv = row['b']
		close_one = get_the_closest_center(av, bv, k_center)
		print(close_one)
		data_lst[close_one].append(row)
	print('-------------------------------------\n\n')
	print(data_lst[0])
	print('-------------------------------------\n\n')
	print(data_lst[1])
	print('-------------------------------------\n\n')
	print(data_lst[2])

data =  pd.read_csv('simpleData.csv')
K = 3
k_center = data.sample(n=K)
assign_points_to_the_closeest_center()
#	Visualize The Data
plt.scatter(data["a"], data["b"],c='red')
plt.scatter(k_center['a'], k_center['b'], c='blue')
plt.xlabel("a")
plt.ylabel('b')
plt.show()
