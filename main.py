import numpy as np

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

def formatData(file):
    global rides
    imRides = []
    rawData = np.genfromtxt(file)
    rideData = np.delete(rawData, 0, axis = 0)
    for index, ride in enumerate(rideData):
        newRide = Ride(index, (ride[0], ride[1]), (ride[2], ride[3]), ride[4], ride[5])
        imRides.append(newRide)

    rides = np.asarray(imRides)
    rides = np.sort(rides, kind = 'heapsort')

if (__name__ == '__main__'):
    formatData('a_example.in')
