#include"kalman.h"
#include<stdlib.h>
#include<stdio.h>
Kalman* newKalman(void){
  Kalman* k = (Kalman*)malloc(sizeof *k);
  return k;
}

void initKalman(Kalman* k, double r, double q, double initVal, double p, double input){
  k->r = r;
  k->q = q;
  k->p = p;
  k->x = initVal;
  k->input = input;
}

void updateKalman(Kalman* kalman, double measurement){
  // Update the current error by taking process error and adding it to the current error in the system.
  kalman->p = kalman->p + kalman->q;
  // Update Kalman Gain to moderate prediction to a sensible range
  kalman->k = kalman->p / (kalman->p + kalman->r);
  // Update the measurement through adding the kalman filtered error (reality vs prediction)
  kalman->x = kalman->x + kalman->k * (measurement - kalman->x);
  // Update the p value. As system goes on, p should get smaller and smaller.
  kalman->p = (1- kalman->k) * kalman->p;
}

//Python wrappers
double getKalmanSensorNoise(Kalman* kalman){
	return kalman->r;
}

double getKalmanProcessNoise(Kalman* kalman){
	return kalman->q;
}

double getKalmanMeasurement(Kalman* kalman){
	return kalman->x;
}

double getKalmanVariance(Kalman* kalman){
	return kalman->p;
}

double getKalmanGain(Kalman* kalman){
	return kalman->k;
}
