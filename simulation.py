import math
import numpy as np

class Simulation(object):
    """docstring for Simulation."""
    def __init__(self, time, cars, rides):
        #super(Simulation, self).__init__()
        self.time = time
        self.cars = cars
        self.rides = rides
        self.freeCars = []
        self.freqVect = []

    def runSimulation(self):
        for t in self.time:
            self.freeCars = []
            for car in self.cars:
                if not car.isBusy:
                    self.freeCars.append(car)
                else:
                    car.move()
            self.dispatch(t)



    def dispatch(self, t):
        #assignedCar = []
        for r in len(self.freeCars):
            self.freqVect = []
            for car in self.freeCars:
                self.freqVect.append(self.findDistance(car, self.rides[r], t))
            assignedCar = self.freqVect.index(min(self.freqVect))
            self.freeCars[assignedCar].updateDestination(self.rides[r].getDestination())
            self.freeCars[assignedCar].changeState()
            self.freeCars[assignedCar].history.append(self.rides[r].rideN)
            self.freeCars.remove(self.freeCars.index(assignedCar))




    def findDistance(self, car, ride, cTime):
        car3d = np.array([car.getLocation[0], car.getLocation[1], cTime])
        destination3d = np.array([ride.getLocation[0], ride.getLocation[1], ride.getTime])
        return np.linalg.norm(car3d-destination3d)
