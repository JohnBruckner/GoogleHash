# import numpy as np

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
        return (startL)

    def getTime(self):
        return startT

class Car:
    carCount = 0

    def __init__(self, carN):
        self.location = (0,0)
        self.destination = (0,0)
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
             changeState

    def changeState(self):
        self.busy = not self.busy

def formatData(file):
    global rides
    global cars

    imRides = []
    imCars = []

    rawData = np.genfromtxt(file)
    rideData = np.delete(rawData, 0, axis = 0)

    for index, ride in enumerate(rideData):
        newRide = Ride(index, (ride[0], ride[1]), (ride[2], ride[3]), ride[4], ride[5])
        imRides.append(newRide)

    rides = np.asarray(imRides)
    rides = np.sort(rides, kind = 'heapsort')

    for i in range(int(rawData.item((0, 2)))):
        imCars.append(Car(i))

    cars = np.asarray(imCars)

if (__name__ == '__main__'):
    formatData('a_example.in')
