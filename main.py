import numpy as np
import simulation

class Ride:
    rideCount = 0

    def __init__(self, rideN, startL, finL, startT, finT):
        self.rideN = rideN
        self.startL = startL
        self.finL = finL
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
        self.location = (0,0)
#<<<<<<< HEAD
        self.destination = (9,9)
#=======
        self.history = []
        self.destination = (0,0)
#>>>>>>> 86902b75a4fa3bbd5597261e54dcb104c17e44eb
        self.carN = carN
        self.busy = False
        Ride.rideCount += 1

    def getLocation(self):
        return self.location

    def move(self):
        if self.location[0] != self.destination[0]:
            if self.location[0] < self.destination[0]:
                self.location[0] += 1
            else:
                self.location[0] -= 1
        elif self.location[1] != self.destination[1]:
            if self.location[1] < self.destination[1]:
                self.location[1] += 1
            else:
                self.location[1] -= 1
        else:
             self.changeState()


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

if (__name__ == '__main__'):
    formatData('b_should_be_easy.in')
    sim = simulation.Simulation(T, cars, rides)
    sim.runSimulation()

    f = open("text.txt", "w")

    for car in cars:
        f.write(str(car.getCarNumber()) + " " + str(car.getCarHistory())+ "\n")
