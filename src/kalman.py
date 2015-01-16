from ctypes import *
lib = cdll.LoadLibrary('./../c_src/libkalman.so')

class Kalman(Structure):
	_fields_ = [("r",c_double),("q",c_double),("x",c_double),("p",c_double),("k",c_double)]
	def __init__(self):
		self.obj = lib.newKalman()
		self.sensor_noise = lib.getKalmanSensorNoise(self.obj)
		self.process_noise = lib.getKalmanProcessNoise(self.obj)
		self.measurement = lib.getKalmanMeasurement(self.obj)
		self.variance = lib.getKalmanVariance(self.obj)
		self.gain = lib.getKalmanGain(self.obj)
	def initKalman(self, r, q, initVal, p, input):
		lib.initKalman(self.obj, r, q, initVal, p, input)
	def updateKalman(self, measurement):
		lib.updateKalman(self.obj, measurement)
		self.sensor_noise = lib.getKalmanSensorNoise(self.obj)
		self.process_noise = lib.getKalmanProcessNoise(self.obj)
		self.measurement = lib.getKalmanMeasurement(self.obj)
		self.variance = lib.getKalmanVariance(self.obj)
		self.gain = lib.getKalmanGain(self.obj)
