import random
import numpy as np
from matplotlib import pyplot as plt
import math
from scipy import stats


def plot(graph_coords, coordinates, index, test_sample, prediciton):
    # plotting training coordinates in blue
    # test coordinate in red
    # nearest neighbour coordinate in green

    #
    fig, ax = plt.subplots()
    x, y = graph_coords.T
    plt.scatter(x, y, color="blue")
    test_x = test_sample[0]
    test_y = test_sample[1]
    plt.scatter(test_x, test_y, color="red")
    plt.annotate(str(prediciton), (test_x, test_y), fontsize="30")

    # adds and labels the axis
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    plt.xlabel("x")
    plt.ylabel("y")

    # gets the nearest neighbour and highlights the point in green
    nearest_x = coordinates[index][0]
    nearest_y = coordinates[index][1]
    plt.scatter(nearest_x, nearest_y, color="green")

    # adding bounds to the axis
    plt.xticks(np.arange(-5, 11, 1.0))
    plt.yticks(np.arange(-5, 11, 1.0))

    # drawing line between the nearest neighbour and the test sample
    x_values = [nearest_x, test_x]
    y_values = [nearest_y, test_y]
    plt.plot(x_values, y_values)

    plt.show()


def insertion_sort():
    pass


# k nearest neighbour prediction method
def k_nearest_neighbours(coordinates, test_sample):

    k = int(input("Enter a value for k: "))

    print("coords")
    print(coordinates)

    # calculate distance from test_sample to all coordinates

    distances = np.zeros([10])
    # print(distances)

    graph_coords = np.delete(coordinates, -1, 1)

    for x in range(0, 10):
        distance = math.sqrt((graph_coords[x][0] - test_sample[0])**2 + (graph_coords[x][1] - test_sample[1])**2)
        distances[x] = distance

    for x in range(k):
        print(x)


    print("Unsorted")
    print(distances)

    print("Sorted")
    # print(np.sort(distances))
    sorted_distances = np.sort(distances)
    print(sorted_distances)
    print("Last k:")

    # returns k smallest distances, k nearest neighbours distances, need to get the index and the label
    smallest_k = sorted_distances[:k]
    print(smallest_k)

    indexes = np.zeros([k])

    # print(indexes)

    x = 0
    for val in smallest_k:
        index = np.where(distances == val)
        indexes[x] = index[0][0]
        x += 1

    print("indexes")
    print(indexes)

    # if 2 points are the same distance away it will not recognise them as different points and just select one
    i = 0
    nearest_labels = np.zeros(k)
    for index in indexes:
        if i == k:
            break
        print(coordinates[int(index)][2])
        nearest_labels[i] = coordinates[int(index)][2]
        i += 1

    print(nearest_labels)

    prediction = int(stats.mode(nearest_labels)[0][0])
    print("PREDICTION: ")
    print(prediction)


# single nearest neighbour prediction method
# this is just KNN with k = 1
def nearest_neighbours(coordinates, test_sample):

    # calculate distance from test_data to all coordinates
    # print("\n= Using NN algorithm =\n")

    distances = np.zeros([10, 1])
    # print(distances)

    graph_coords = np.delete(coordinates, -1, 1)

    for x in range(0, 10):
        distance = math.sqrt((graph_coords[x][0] - test_sample[0])**2 + (graph_coords[x][1] - test_sample[1])**2)
        distances[x] = distance
        # print(distance)

    # find index of shortest distance in distances then return label of same index in coordinates.
    # some sort of search
    # print("MIN: " + str(np.amin(distances)))
    # change this to take k values
    index = np.where(distances == np.amin(distances))
    index = index[0][0]

    # then look at labels of k values and decide prediction
    prediction = coordinates[index][2]
    # print(coordinates[index])
    print("\n= NN PREDICTION =\n")
    print(prediction)

    plot(graph_coords, coordinates, index, test_sample, prediction)


# generate random coordinate training pairs and single coordinate test pair
def generate_samples():

    # initialises a numpy array with 10 coordinate paris full of 0s
    # last column is used to store the label saying whether it is positive (1) or negative (-1) (below or equal to 0)
    # e.g. coordinates [6, -2] in the array would be [6, -2, -1], where the -1 indicates it is negative
    coordinates = np.zeros([10, 3])

    # creates 10 random coordinates and fills in the numpy array, labelling them if they are negative or positive
    for x in range(10):
        x_val = random.randint(-3, 10)
        y_val = random.randint(-3, 10)

        if x_val <= 0 or y_val <= 0:
            label = -1
        else:
            label = 1

        coordinate = [x_val, y_val, label]
        coordinates[x] = coordinate

    # print(coordinates)

    test_sample = [random.randint(-3, 10), random.randint(-3, 10), 0]
    # print("Test: " + str(test_sample))

    nearest_neighbours(coordinates, test_sample)
    k_nearest_neighbours(coordinates, test_sample)


def main():
    print("\n= ML Batch supervised learning (binary classification) using KNN algorithm via transduction =\n")
    generate_samples()

main()