import numpy as np

#Class solely meant to keep track of data points related to time for each Mat. Meant as a subdivision class for each Mat in line
class Mat(object):
	width = 64
	height = 8
	
	def __init__(self, x = 0, y = 0):
		self.pos = (x,y)
		dims = (self.width, self.height)
		#Substitute empty for zeros if you want a slightly, SLIGHTLY faster method. However, remember that it might mess up some of your other code
		self.data_points = np.zeros(dims, dtype=np.int)
	def update(self, arr, x=-1, y=-1):
		if x == -1 or y == -1:
			#Need to to arr casts
			self.data_points = np.array(arr, dtype=np.int)
		else:
			self.data_points[x,y] = int(arr)
        def poll(self):
            return self.data_points
