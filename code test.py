
import csv
from collections import defaultdict
import sys
import math
from array import array
from array import *
from turtle import distance


filename ="CrocData.csv"
size = 100



class monitor():
    # list_of_locations =[]
    # edges_data = []
    # num_of_sightings = []
    # sortedarry = []
    # elements = num_of_sightings

    def __init__(self, size):
        self.distance_data = []
#        self.dist = []
        self.list_of_locations = []
        self.locations = []
        self.edges_data = []
        self.num_of_sightings= []
        self.matrix = [[0 for x in range(size)]for y in range(size)]
        self.nodepoints=[]
        self.cords = []
        self.gdist = []
        self.graph = {}
        self.readData()

    # ''' Finds the distance between each connected edge in the map'''
    # def find_distance():
    #     distance = []
    #     cords = cm.cords
    #     for i in range(0, ((len(cords)) - 1)):
    #         # distance = ((cm.dis[i][0] - cm.dis[i+1][0])**2 + (cm.dis[i][1] - cm.dis[i+1][1])**2)**0.5)
    #         cm.gdist.append(distance)




    ''' Reads the data from the crocdata file into a set of corresponding lists'''
    def readData(self):
        with open(filename,'r') as data:
                        csv_data_reader = csv.reader(data)
                        index = 0
                        next(csv_data_reader)
                        for line in csv_data_reader:
                            if line[0] != '':
                                nodenum = int(line[0])   #define column data as line
                                x = float(line[1])
                                y = float(line[2])
                                env = int(line[3])
                                numsight = int(line[4])

                            edgea = int(line[5])
                            edgeb = int(line[6])
                            water = line[7]
                            gdist= line[8]

                            self.list_of_locations .append([nodenum, x, y, env, numsight, edgea, water, gdist])
                            self.cords.append([x,y])
                            self.edges_data .append([edgea, edgeb, water])
                            self.num_of_sightings.append(numsight)
                            self.distance_data .append([nodenum,edgea,gdist])
                            self.graph[nodenum] = []
                            if not nodenum in self.nodepoints:
                                self.nodepoints.append(nodenum)
                            index += 1


        data.close



read = monitor(50)




#bubblesort in decendind order
def Bubble_Sort(unsorted_list):

    for i in range(0,len(unsorted_list)-1):
        for j in range(len(unsorted_list)-1):
            if(unsorted_list[j]<unsorted_list[j+1] ):
                temp_storage = unsorted_list[j]
                unsorted_list[j] = unsorted_list[j+1]
                unsorted_list[j+1] = temp_storage


    return unsorted_list

cm=monitor(size)
unsorted_list = cm.num_of_sightings



''' Finds the distance between each edge on graph. There are some '''
def find_distance():
    distance = []
    cords = cm.cords
    edges = cm.edges_data
    for count, edge in enumerate(edges):
        x1 = cords[edge[0]-1][0]
        y1 = cords[edge[0]-1][1]

        x2 = cords[edge[1]-1][0]
        y2 = cords[edge[1]-1][1]

        # distance = ((cm.dis[i][0] - cm.dis[i+1][0])**2 + (cm.dis[i][1] - cm.dis[i+1][1])**2)**0.5
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        cm.gdist.append(distance)
        cm.edges_data[count].insert(2,distance)

        print(
            f"{count} distance between node: {edge[0]} : x1: {cm.cords[edge[0]-1][0]} y1: {cm.cords[edge[0]-1][1]} and node: {edge[1]} : x2: {cm.cords[edge[1]-1][0]} y2: {cm.cords[edge[1]-1][1]} is {distance}")


find_distance()



# def location_check(self, a, b):
    
#         if (a == cm.cords[0] and b == cm.cords[0]):
            
#             print('location is already in databasename')
#             return 
#         else:
#             print('location is not in databasename')




    # def find_distance(self, geoid,search_site):
    #     if geoid == self.list_of_locations[0]:
    #         while search_site == self.search_locations[0]:
    #             x = self.list_of_locations[1]
    #             y = self.list_of_locations[2]
    #             x1 = search_locations[0]
    #             x2 = search_locations[1]
    #             dis = math.sqrt(((x-x1)**2)+ ((y-y1)**2) )


    #     # dis = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )




#bubblesort in decendind order
def Bubble_Sort(unsorted_list):

    for i in range(0,len(unsorted_list)-1): 
        for j in range(len(unsorted_list)-1): 
            if(unsorted_list[j]<unsorted_list[j+1] ):  
                temp_storage = unsorted_list[j] 
                unsorted_list[j] = unsorted_list[j+1] 
                unsorted_list[j+1] = temp_storage 
    return unsorted_list 
cm=monitor(size)
unsorted_list = cm.num_of_sightings


# #bubblesort in ascendind order
# def Bubble_Sort(unsorted_list):

#     for i in range(0,len(unsorted_list)-1): 
#         for j in range(len(unsorted_list)-1): 
#             if(unsorted_list[j]>unsorted_list[j+1] ):  
#                 temp_storage = unsorted_list[j] 
#                 unsorted_list[j] = unsorted_list[j+1] 
#                 unsorted_list[j+1] = temp_storage 
#     return unsorted_list 
# cm=monitor(size)
# unsorted_list = cm.num_of_sightings



# A class to represent a graph object
class Graph:
    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge (x, y, w) represents an edge from `x` to `y` having weight `w`
    edges = cm.edges_data
    n=len(cm.edges_data)
    # Constructor to construct a graph
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [None] * n
 
        # allocate memory for the adjacency list
        for i in range(n):
            self.adjList[i] = []
 
        # add edges to the directed graph
        for (src, dest, weight) in edges:
            # allocate node in adjacency list from src to dest
            self.adjList[src].append((dest, weight))
 
 
# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print current vertex and all its neighboring vertices
        for (dest, weight) in graph.adjList[src]:
            print(f'({src} —> {dest}, {weight}) ', end='')
        print()        #uncomment to print one after another 
 
 



if __name__ == '__main__':
    cm=monitor(size)
    edges=cm.edges_data
    n=len(cm.edges_data)
    g=Graph
    
    # print (cm.list_of_locations)
    # print (cm.nodepoints)
    # user_location = input ("Enter your location")
    max_sight = max(cm.list_of_locations, key=lambda row: str(row[4]))
   
    print('\n')
    print('Previous max sighting')
    print('\nLocation index:',max_sight[0],'\nx:',max_sight[1],'\ny:',max_sight[2],'\nnumber of Previous sightings:',max_sight[4])
    
    # loc1= str(input('Please enter your location in x co ordinate: '))
    # loc2= str(input('Please enter your location in y co ordinate: '))
    # # print(location_check(loc1,loc2))


    # print(max_sight)
    print('\n')
    print('\n')
    print('list of location data :')
    print(cm.list_of_locations)

    print('\n')
    print('\n')
 
    # print adjacency list representation of the graph
    print('co ordinate data :')
    print(cm.cords)
    # distance b/w a and b
    print('\n')
    print('\n')
    # print list of edges with their weights
    print('list of edges with their weights :')
    print(cm.edges_data)
    print('\n')
    print('\n')

    # # construct a graph from a given list of edges
    graph = Graph(edges, n)
 
    # print adjacency list representation of the graph
    printGraph(graph)
    print('\n')

    print('\n')
    print('x y data paased for distance calculation')
    for i in range (((len(cm.cords)-1))):
            print(f"{i} x1: {(cm.cords[i][0])} x2: {(cm.cords[i+1][0])} y1: {(cm.cords[i][1])} y2: {(cm.cords[i+1][1])}")
    print('\n')
    print('\n')

    print('\n')
    print('distance between x and y in linear algorithm :')
    find_distance()
    # for i in range ((len(cm.gdist))):
    #         print(f"distance between x1: {cm.cords[i][0]} y1: {cm.cords[i][1]} and x2: {cm.cords[i+1][0]} y2: {cm.cords[i+1][1]} is {cm.gdist[i]}")
    
    # print(cm.dist[-1])

    print('\n')
    
    # print('sorted number of sightings is')
    # cm.num_of_sightings.sort()
    # print(cm.num_of_sightings)

    print("\r")
# using sorted and lambda to print list sorted
# by in descending order
# cm.bubbleSort(arr)
#     print("Sorted array is:")
#     for i in range(len(arr)):
#         print("% d" % arr[i], end=" ")   
    print("Sorted list is, ")
    print("Sorted List using Bubble Sort Technique: ",Bubble_Sort(unsorted_list))
    print("no of sorted: ",len(Bubble_Sort(unsorted_list)))
    print("\r")
