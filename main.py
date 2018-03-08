import numpy as np  # for array stuff
# import scipy.spatial  # for voronoi map generator
import sklearn.cluster  # for clustering and data analysis
import re  # for output file formatting
# import matplotlib.pyplot as plt
import simulation  # where some of the magic happens


class mapOptimizer:

    def __init__(self, rides):
        self.rides = rides
        self.rideStartL = np.array([[0, 0]])
        # self.clusterCentres = self.c.cluster_centers_

    def findStartL(self):
        for ride in self.rides:
            newShape = np.expand_dims(ride.startL, axis=0)
            print(str(newShape.shape))
            print((str(self.rideStartL.shape)))
            #np.append(self.rides, newShape)
            self.rideStartL = np.vstack((self.rideStartL, ride.startL))

    def clustering(self):
        self.c = sklearn.cluster.KMeans(n_clusters=1, init='k-means++', n_init=20, max_iter=1000, verbose=1, n_jobs=-1,
                                        algorithm='auto')
        self.c.fit(self.rideStartL)

    def closestCluster(self, point):
        point = np.expand_dims(point, axis=0)
        index = self.c.predict(point)
        return index

    def closestClusterCoordinates(self, index):
        coordinates = self.c.cluster_centers_[index]
        return coordinates


class Ride:
    rideCount = 0

    def __init__(self, rideN, startL, finL, startT, finT):
        self.rideN = rideN
        self.startL = np.array(startL)
        self.finL = np.array(finL)
        self.startT = startT
        self.finT = finT
        Ride.rideCount += 1

    def __lt__(self, other):
        return self.startT < other.startT

    def __str__(self):
        return "Ride Number: " + str(self.rideN)


class Car:
    carCount = 0

    def __init__(self, carN):
        self.carN = carN
        self.gotToPickup = False
        self.busy = False
        self.pickUpTime = 0
        self.currentTime = 0
        self.location = np.array([0, 0])
        self.pickUp = np.array([9, 9])
        self.destination = np.array([9, 9])
        self.centroid = np.array([0, 0])
        self.history = []
        Ride.rideCount += 1

    def changeState(self):
        self.busy = not self.busy

    def updateCar(self, pickup=[], destination=[], centroid=[], centre=True):
        if centre:
            self.centroid = centroid
            self.busy = False
        else:
            self.busy = True
            self.pickUp = pickup
            self.destination = destination

    def move(self, destination):
        if not np.array_equal(self.location[0], destination[0]):
            #print(str(self.location.shape))
            #print(str(self.location[0]))
            if self.location.item(0) < destination.item(0):
                self.location[0] += 1
                # return True
            else:
                self.location[0] -= 1
                # return True
        elif np.array_equal(self.location[1], destination[1]):
            if self.location.item(1) < destination.item(1):
                self.location[1] += 1
                # return True
            else:
                self.location[1] -= 1
                # return True
        # return False

    def goToCentroid(self):
        self.busy = False
        self.move(self.centroid)

    def goToPickup(self):
        self.busy = True
        self.move(self.pickUp)

    def goToDestination(self):
        self.busy = True
        self.move(self.destination)

    def route(self, currentTime):
        if self.busy == False:
            self.goToCentroid()
        else:
            if self.gotToPickup == False or self.pickUpTime >= currentTime:
                self.goToPickup()
                if (self.location == self.pickUp).all():
                    self.gotToPickup = True
            else:
                if  (self.location == self.destination).all():
                    self.busy = False
                else:
                    self.goToDestination()


# def move(self, currentTime):
#     if len(self.pickUp) == 0:
#         # print('DEEEEEEEEEEZ NUTS')
#         if self.route(self.destination):
#             pass
#             # self.changeState()
#     elif self.pickUpTime >= currentTime:
#         pass
#     else:
#         # print('YIPPEE KAY YAY MOTHERFUKCER')
#         print(self.pickUp)
#         if self.route(self.pickUp):
#             self.pickUp = []
#
# def route(self, destination):
#     print(self.location)
#     print(destination)
#     if self.location[0] != destination[0]:
#         if self.location[0] < destination[0]:
#             self.location[0] += 1
#             return True
#         else:
#             self.location[0] -= 1
#             return True
#     elif self.location[1] != destination[1]:
#         if self.location[1] < destination[1]:
#             self.location[1] += 1
#             return True
#         else:
#             self.location[1] -= 1
#             return True
#     return False
#
# def isAtDestination(self):
#     return self.destination == self.location
#
# def updateDestination(self, dest):
#     self.destination = dest
#
# def getLocation(self):
#     return self.location
#
# def isBusy(self):
#     return self.busy
#
# def getHistory(self):
#     return self.history
#
# def getCarNumber(self):
#     return self.carN
#
# def getCarHistory(self):
#     return self.history


def formatData(file):
    global rides
    global cars
    global B
    global T

    imRides = []
    imCars = []

    rawData = np.genfromtxt(file)
    rideData = np.delete(rawData, 0, axis=0)

    B = int(rawData.item((0, 4)))
    T = int(rawData.item((0, 5)))

    for index, ride in enumerate(rideData):
        newRide = Ride(index, (ride[0], ride[1]), (ride[2], ride[3]), ride[4], ride[5])
        imRides.append(newRide)

    rides = np.asarray(imRides)
    rides = np.sort(rides, kind='heapsort')

    for i in range(int(rawData.item((0, 2)))):
        imCars.append(Car(i))

    cars = np.asarray(imCars)




if (__name__ == '__main__'):
    formatData('a_example.in')
    map = mapOptimizer(rides)
    map.findStartL()
    sim = simulation.Simulation(T, cars, rides, map)
    sim.runSimulation()
    print("Hello world!")
    print(str(len(rides)))
    print(str(sim.ridesDropped))
    # n_clusters = len(map.clusterCentres)
    # k_means_cluster_centers = np.sort(map.clusterCentres, axis=0)
    # k_means_labels = pairwise_distances_argmin(X, k_means_cluster_centers)
    # fig = plt.figure(figsize=(8, 3))
    # fig.subplots_adjust(left=0.02, right=0.98, bottom=0.05, top=0.9)
    # colors = ['#4EACC5', '#FF9C34', '#4E9A06']
    # ax = fig.add_subplot(1, 3, 1)
    # for k, col in zip(range(n_clusters), colors):
    #     my_members = k_means_labels == k
    #     cluster_center = k_means_cluster_centers[k]
    #     # ax.plot(rides.startL[my_members, 0], rides[my_members, 1], 'w',
    #     #         markerfacecolor=col, marker='.')
    #     ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
    #             markeredgecolor='k', markersize=6)
    # ax.set_title('KMeans')
    # ax.set_xticks(())
    # ax.set_yticks(())
    # colors = ['#4EACC5', '#FF9C34', '#4E9A06']
    # plt.show()
    f = open("a2.txt", "w")
    # f.write("PENIS")

    for car in cars:
        s = str(car.history)
        s = re.sub(r'[^\w]', ' ', s)
        s = re.sub(' +', ' ', s)
        s = s.strip(" ")
        f.write(str(len(car.history)) + " " + s + "\n")

    f.close()
