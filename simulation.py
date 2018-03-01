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

    def runSimulation(self):
        for t in self.time:
            for car in self.cars:
                if not car.isBusy:
                    freeCars.append(car)
                else:
                    car.move()

    def findDistance(self, car, ride, cTime):
        car3d = np.array([car.getLocation[0], car.getLocation[1], cTime])
        destination3d = np.array([ride.getLocation[0], ride.getLocation[1], ride.getTime])
        return np.linalg.norm(car3d-destination3d)
