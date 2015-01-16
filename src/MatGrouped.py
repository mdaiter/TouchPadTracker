import numpy as np
import kmeans
import Mat

class MatGrouped(object):
    #define overall width
    width = 64
    #define overall height
    height = 8
    #initialize mats. Let's start Kalman filters and kmeans
    #Basically, pipeline: input -> kmeans -> kalman filters -> outputs
    def __init__(self, mats_init=[]):
        print "Initializing MatGrouped"
        self.mats = mats_init
        for mat in self.mats:
            if mat.pos[0] > 0:
                self.width += mat.pos[0]
            if mat.pos[1] > 0:
                self.height += mat.pos[1]
    
    def update(self, inp):
        for mat in self.mats:
            arr = inp.read_input(width=mat.width, height=mat.height)
            print "Mat updating with: " 
            print arr
            mat.update(arr)
    #Polls for points. Update cluster count as necessary.
    def poll(self, num_clusters=2, threshold=0):
        #For storing points in [x,y] format for weighting 
        total_mat = np.zeros((1,2)).astype('float32')
        #Needed for replacing first zeros
        found_first = False
        ##Generate entire array
        for mat in self.mats:
            #Poll
            temp_mat = mat.poll().astype('float32')
            print temp_mat
            for (x,y), value in np.ndenumerate(temp_mat):
                    if value > threshold:
                        if not found_first:
                            total_mat = np.append(total_mat, [[x, y]], axis=0)
                        else:
                            total_mat = np.array([[x,y]])
                            found_first = True
        #Instantiate kmeans, w/total mat as first parameter, number of clusters as second, and number of iterations for accuracy as third
        [clusters, indices] = kmeans.kmeans(total_mat, num_clusters, 10)
        return clusters
    def append(self, mat_append):
        for mat in self.mats:
            if mat.pos[0] == mat_append.pos[0] and mat.pos[1] == mat_append.pos[1]:
                mat = mat_append
                return
        self.mats.append(mat_append)
