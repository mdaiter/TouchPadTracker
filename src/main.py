import numpy as np
import cv2
import MatGrouped
import Mat
import Foot
import Input
import time
import FootTracker

if __name__ == "__main__":
    foot_tracker = FootTracker.FootTracker()
    inp = Input.Input()
    #Clear serialport data that could be fucking with the system
    inp.ser.read(10000)

    #Need to make a mat to pull values from
    mat = Mat.Mat()
    mat.width = 16
    mat.height = 5
    foot_tracker.mat_tracker.append(mat)
    while True:    
        ##Update mats in Foot_Tracker
        foot_tracker.mat_tracker.update(inp)
        ##Poll for different values
        foot_tracker.update()
        print 'Updated foot tracker with left hand values ',  foot_tracker.left_foot.estimated_pos[0], ' and ',  foot_tracker.left_foot.estimated_pos[1]
        print 'Updated foot tracker with right hand values ',  foot_tracker.right_foot.estimated_pos[0], ' and ',  foot_tracker.right_foot.estimated_pos[1]
        #time.sleep(0.5)
