# import math
import main
import numpy as np
import math


class Simulation(object):
    """docstring for Simulation."""

    def __init__(self, time, cars, rides, map):
        # super(Simulation, self).__init__()
        self.time = time  # time given for simulation
        self.cars = cars  # list of cars with their respective locations
        self.rides = rides  # list of rides
        self.freeCars = []
        self.freqVect = []
        self.map = map

    def runSimulation(self):
        print("No. of rides: " + str(len(self.rides)))
        self.map.clustering()
        for t in range(self.time):
            self.freeCars = []
            print("Time: " + str(t))
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
            if len(self.rides) == 0:
                print("Simulation ended!")
                break
            print("Dispatching")
            self.dispatch(t)
        print("Simulation ended!")

    def dispatch(self, t):
        # assignedCar = []
        l = len(self.freeCars)
        print("\n")
        if len(self.rides) == 0:
            print("No rides left!")
            pass
        else:
            for r in range(len(self.freeCars)):
                i = self.map.closestCluster(self.freeCars[r].location)
                centroid = self.map.closestClusterCoordinates(i)
                print("Ride: " + str(r))
                self.freqVect = []
                for car in self.freeCars:
                    try:
                        self.freqVect.append(self.findDistance(car, self.rides[r], t))
                    except:
                        pass
        self.rides[r].startL, self.rides[r].fin        try:
                    assignedCar = self.freqVect.index(min(self.freqVect))
                    # print(type(assignedCar))
                    #print("Assigned car: " + str(assignedCar))
                    if self.distance2D(car, self.rides[r]) < self.rides[r].finT - t:
                        print("Dropping ride: " + str(self.rides[r]))
                        self.freeCars[assignedCar].updateCar(centre=True)
                        self.freeCars[assignedCar].route(centroid, t)
                        del self.rides[r]
                    else:
                        self.freeCars[assignedCar].pickUpTime = self.rides[r].startT
                        self.freeCars[assignedCar].updateCar(pickup = self.rides[r].startL, destination = self.rides[r].finL, centre=False)
                        self.freeCars[assignedCar].route(centroid, t)
                        print("Car no: " + str(self.freeCars[assignedCar].carN) + " Took ride: " + str(
                            self.rides[r].rideN))
                        self.freeCars[assignedCar].history.append(self.rides[r].rideN)
                        # print("Free cars: " + str(self.freeCars))
                        # print("Free cars index: " + str(self.freeCars[assignedCar]))
                        del self.freeCars[assignedCar]
                except:
                    pass
        self.rides = self.rides[l:]

    def distance2D(self, car, ride):
        return math.fabs(car.location[0] - ride.startL[0]) + math.fabs(car.location[1] - ride.startL[1]) + math.fabs(
            ride.startL[0] - ride.finL[0]) + math.fabs(ride.startL[1] - ride.finL[0])

    def findDistance(self, car, ride, cTime):
        # print(str(type(car.location)))
        # print(str(type(ride.startL)))
        car3d = np.array([car.location[0], car.location[1], cTime])
        destination3d = np.array([ride.startL[0], ride.startL[1], ride.finT])
        # print(str(car3d))
        # print(str(destination3d))
        return np.linalg.norm(car3d - destination3d)
