import matplotlib.pyplot as plt
import cv2
from store_layout import find_store
import numpy as np
#from matplotlib.ticker import FormatStrFormatter


def draw(optimal_path, image_path, newimage, address):

	store_layout = find_store(address)

	image = cv2.imread(image_path,0)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	for i in range(len(optimal_path)-1):

		#one, two = optimal_path[i],optimal_path[i+1]
		one, two = store_layout[optimal_path[i]], store_layout[optimal_path[i+1]]
		
		image = cv2.line(image, one, two, (33,136,56), 6)  
		image = cv2.circle(image, one, 3, ( 0, 86, 179), 10)  

	else:
		image = cv2.circle(image, store_layout[optimal_path[i+1]], 3, ( 0, 86, 179), 10) 
		image = cv2.circle(image, store_layout[optimal_path[0]], 3, ( 0, 86, 179), 10)   
		#image = cv2.circle(image, optimal_path[i+1], 5, ( 0, 86, 179), 20)  

	print("DONE")
	cv2.imwrite(newimage, image)