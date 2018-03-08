import numpy as np
import simulation
import math
import re

class Ride:
    rideCount = 0

    def __init__(self, rideN, startL, finL, startT, finT):
        self.rideN = rideN
        self.startL = list(startL)
        self.finL = list(finL)
        self.startT = startT
        self.finT = finT
        Ride.rideCount += 1

    def __lt__(self, other):
        return self.startT < other.startT

    def __str__(self):
        return "Ride Number: " + str(self.rideN)

    def getLocation(self):
        return (self.startL)

    def getTime(self):
        return (self.startT)

    def getDestination(self):
        return self.finL

class Car:
    carCount = 0

    def __init__(self, carN):
        self.location = [0,0]
        self.destination = [9,9]
        self.history = []
        self.carN = carN
        self.busy = False
        self.pickUp = []
        self.pickUpTime = 0
        #self.currentTime = 0
        Ride.rideCount += 1

    def getLocation(self):
        return self.location

    def move(self, currentTime):
        if len(self.pickUp) == 0:
            print('DEEEEEEEEEEZ NUTS')
            if self.route(self.destination):
                self.changeState()
        elif self.pickUpTime >= currentTime:
            pass
        else:
            print('YIPPEE KAY YAY MOTHERFUKCER')
            print(self.pickUp)
            if self.route(self.pickUp):
                self.pickUp = []

    def route(self, destination):
        print(self.location)
        print(destination)
        if self.location[0] != destination[0]:
            if self.location[0] < destination[0]:
                self.location[0] += 1
                return True
            else:
                self.location[0] -= 1
                return True
        elif self.location[1] != destination[1]:
            if self.location[1] < destination[1]:
                self.location[1] += 1
                return True
            else:
                self.location[1] -= 1
                return True
        return False


    def isAtDestination(self):
        return self.destination == self.location

    def updateDestination(self, dest):
        self.destination = dest

    def getLocation(self):
        return self.location

    def isBusy(self):
        return self.busy

    def changeState(self):
        self.busy = not self.busy

    def getHistory(self):
        return self.history

    def getCarNumber(self):
        return self.carN

    def getCarHistory(self):
        return self.history


def formatData(file):
    global rides
    global cars
    global B
    global T
    global meanPoint


    imRides = []
    imCars = []

    rawData = np.genfromtxt(file)
    rideData = np.delete(rawData, 0, axis = 0)

    B = int(rawData.item((0, 4)))
    T = int(rawData.item((0, 5)))

    for index, ride in enumerate(rideData):
        newRide = Ride(index, (ride[0], ride[1]), (ride[2], ride[3]), ride[4], ride[5])
        imRides.append(newRide)

    rides = np.asarray(imRides)
    rides = np.sort(rides, kind = 'heapsort')

    for i in range(int(rawData.item((0, 2)))):
        imCars.append(Car(i))

    cars = np.asarray(imCars)
    #meanPoint = findMean()

# def findCentroid():
#     #minDist = float("inf")
#     point = np.array([0, 0])
#     for ride in rides:
#         pass
#     return point


if (__name__ == '__main__'):
    formatData('c_no_hurry.in')
    sim = simulation.Simulation(T, cars, rides, meanPoint)
    sim.runSimulation()
    print("Hello world!")
    f = open("c.txt", "w")
    #f.write("PENIS")

    for car in cars:
        s = str(car.history)
        s = re.sub(r'[^\w]', ' ', s)
        s = re.sub(' +',' ', s)
        s = s.strip(" ")
        f.write(str(len(car.history)) + " " + s + "\n")

    f.close()
