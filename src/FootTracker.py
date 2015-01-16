import numpy as np
import cv2
import MatGrouped
import Foot
import Input

#Foot Tracker. Should start to track feet across pressure mat using Kalman Filter. Two dimensional. Two vectors.
class FootTracker(object):

    def __init__(self, mats=[]):
        #Need the MatTracker
        self.mat_tracker = MatGrouped.MatGrouped(mats)
        #There are two clusters in this example.
        clusters = self.mat_tracker.poll(2, 600)
        #Need to make two feet...
        if clusters[0][0] < clusters[1][0]:
            self.left_foot = Foot.Foot(clusters[0][0], clusters[0][1])
            self.right_foot = Foot.Foot(clusters[1][0], clusters[1][1])
        else:
            self.left_foot = Foot.Foot(clusters[1][0], clusters[1][1])
            self.right_foot = Foot.Foot(clusters[0][0], clusters[0][1])
        ##Start tracking....
    def update(self):
        #There are two clusters in this example.
        clusters = self.mat_tracker.poll(2, 600)
        #Need to make two feet...
        if clusters[0][0] < clusters[1][0]:
            self.left_foot.update(clusters[0][0], clusters[0][1])
        else:
            self.right_foot.update(clusters[1][0], clusters[1][1])

if __name__ == "__main__":
    foot_tracker = FootTracker()
    inp = Input.Input()
    #Clear serialport data that could be fucking with the system
    inp.ser.read(10000)
    while True:    
        ##Update mats in Foot_Tracker
        foot_tracker.mat_tracker.update(inp)
        ##Poll for different values
        foot_tracker.update()
        print 'Updated foot tracker with values ',foot_tracker.left_foot.estimated_pos[0], ' and ', foot_tracker.right_foot.estimated_pos[1]
