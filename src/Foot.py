import numpy as np
import cv2
from kalman2d import Kalman2D

class Foot(object):
    def __init__(self, x=0.0, y=0.0):
        #Let's also assume that the foot isn't moving. Just to make things easier.
        self.vector = [0,0]
    #Initialize each foot w/zero, zero to make sure we can tell initialization
        self.estimated_pos = [x,y]
        self.raw_pos = [x,y]
    #Need a previous position for calculating 
        self.prev_pos = [x,y]
    #Finally, ALWAYS base things with estimation. Therefore, use a Kalman filter
        self.kalman_pos = Kalman2D(x,y)
        self.update(x,y)
    def update(self, x, y):
        self.prev_pos = self.estimated_pos
        self.kalman_pos.update(x, y)
        self.raw_pos = [x, y]
        est_pos = self.kalman_pos.getEstimate()
        self.estimated_pos = [est_pos[0], est_pos[1]]
        self.calcVector()
    def calcVector(self):
        self.vector[0] = self.estimated_pos[0] - self.prev_pos[0]
        self.vector[1] = self.estimated_pos[1] - self.prev_pos[1]
    def returnEstimate(self):
        return [(c) for c in self.kalman_pos.getEstimate()]
	
