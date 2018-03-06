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
        print("No. of rides: " + str(len(self.rides)))
        for t in range(self.time):
            self.freeCars = []
            for car in self.cars:
                print("Car is: " + str(car.busy) + " " + str(car.carN))
                if not car.busy:
                    print("Car: " + str(car.carN) + " is free and getting new assignment")
                    self.freeCars.append(car)
                    print(str(len(self.freeCars)))
                else:
                    print(str(car.busy))
                    print("Car: " + str(car.carN) + " is moving")
                    car.move(t)
                    print(str(car.location))
            print("Dispatching")
            self.dispatch(t)


    def dispatch(self, t):
        #assignedCar = []
        l = len(self.freeCars)
        print("\n")
        if len(self.rides) == 0:
            print("No rides left!")
            pass
        else:
            for r in range(len(self.freeCars)):
                print("Ride: " + str(r))
                self.freqVect = []
                for car in self.freeCars:
                    self.freqVect.append(self.findDistance(car, self.rides[r], t))
                assignedCar = self.freqVect.index(min(self.freqVect))
                #print(type(assignedCar))
                print("Assigned car: " + str(assignedCar))
                self.freeCars[assignedCar].pickUpTime = self.rides[r].startT
                self.freeCars[assignedCar].pickUp = self.rides[r].startL
                self.freeCars[assignedCar].updateDestination(self.rides[r].finL)
                self.freeCars[assignedCar].changeState()
                print("Car no: " + str(self.freeCars[assignedCar].carN) + " Took ride: " + str(self.rides[r].rideN))
                self.freeCars[assignedCar].history.append(self.rides[r].rideN)
                #print("Free cars: " + str(self.freeCars))
                #print("Free cars index: " + str(self.freeCars[assignedCar]))
                del self.freeCars[assignedCar]
        self.rides = self.rides[l:]



    def findDistance(self, car, ride, cTime):
        #print(str(type(car.location)))
        #print(str(type(ride.startL)))
        car3d = np.array([car.location[0], car.location[1], cTime])
        destination3d = np.array([ride.startL[0], ride.startL[1], ride.finT])
        #print(str(car3d))
        #print(str(destination3d))
        return np.linalg.norm(car3d-destination3d)
