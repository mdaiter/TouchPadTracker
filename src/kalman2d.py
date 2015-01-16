import cv

class Kalman2D(object):
    '''
    A class for 2D Kalman filtering
    '''

    def __init__(self, x=0.0, y=0.0, processNoiseCovariance=1e-4, measurementNoiseCovariance=1e-1, errorCovariancePost=0.1):
        '''
        Constructs a new Kalman2D object.  
        For explanation of the error covariances see
        http://en.wikipedia.org/wiki/Kalman_filter
        '''

        self.kalman = cv.CreateKalman(4, 2, 0)
        self.kalman_state = cv.CreateMat(4, 1, cv.CV_32FC1)
        self.kalman_process_noise = cv.CreateMat(4, 1, cv.CV_32FC1)
        self.kalman_measurement = cv.CreateMat(2, 1, cv.CV_32FC1)

	self.kalman_measurement[0, 0] = x
	self.kalman_measurement[1, 0] = y

	for j in range(4):
            for k in range(4):
                self.kalman.transition_matrix[j,k] = 0
            self.kalman.transition_matrix[j,j] = 1

        cv.SetIdentity(self.kalman.measurement_matrix)

        cv.SetIdentity(self.kalman.process_noise_cov, cv.RealScalar(processNoiseCovariance))
        cv.SetIdentity(self.kalman.measurement_noise_cov, cv.RealScalar(measurementNoiseCovariance))
        cv.SetIdentity(self.kalman.error_cov_post, cv.RealScalar(errorCovariancePost))

        self.predicted = None
    
    def update(self, x, y):
        '''
        Updates the filter with a new X,Y measurement
        '''

        self.kalman_measurement[0, 0] = x
        self.kalman_measurement[1, 0] = y

        self.predicted = cv.KalmanPredict(self.kalman)
        self.corrected = cv.KalmanCorrect(self.kalman, self.kalman_measurement)

    def getEstimate(self):
        '''
        Returns the current X,Y estimate.
        '''

        return self.corrected[0,0], self.corrected[1,0]

    def getPrediction(self):
        '''
        Returns the current X,Y prediction.
        '''

        return self.predicted[0,0], self.predicted[1,0]
