
import csv
from collections import defaultdict
import sys
import math
from array import array
from array import *


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
        self.list_of_locations = []
        self.edges_data = []
        self.num_of_sightings= []
        self.matrix = [[0 for x in range(size)]for y in range(size)]
        self.nodepoints=[]
        self.readData()
        self.graph = defaultdict(list)

    def readData(self):    
        with open(filename,'r') as data:
                        csv_data_reader = csv.reader(data)
                        index = 0
                        next(csv_data_reader)
                        for line in csv_data_reader:
                            nodenum = line[0]   #define column data as line
                            x = line[1]
                            y = line[2]
                            env = line[3]
                            numsight = line[4]
                            edgea = line[5]
                            water = line[6]
                            gdist= line[7]
                            
                            self.list_of_locations .append([nodenum, x, y, env, numsight, edgea, water, gdist])
                            self.edges_data .append([nodenum, edgea])
                            self.distance_data .append([nodenum,edgea,gdist])
                            if line[0] != '':
                                self.num_of_sightings .append([numsight])
                            if not nodenum in self.nodepoints:
                                self.nodepoints.append(nodenum)
                            index += 1
    
                            
        data.close





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


    


class graph:


    def build_graph():
        cm=monitor(size)
        for i in range (len(cm.edges_data)):
            edges = cm.edges_data
        
            graph = defaultdict(list)
        
        # Loop to iterate over every
        # edge of the graph
            for edge in edges:
                a, b = edge[0], edge[1]
            
            # Creating the graph
            # as adjacency list
                graph[a].append(b)
                graph[b].append(a)
            return graph 

    

    


if __name__ == '__main__':
    cm=monitor(size)
    g=graph
    
    
    # print (cm.list_of_locations)
    # print (cm.nodepoints)
    # user_location = input ("Enter your location")
    max_sight = max(cm.list_of_locations, key=lambda row: str(row[4]))
    print('\n')
    print('Previous max sighting')
    print('\nLocation:',max_sight[0],'number of Previous sightings:',max_sight[4])
    # print(max_sight)
    print('\n')
    print('\n')
    print('list of location data :')
    print(cm.list_of_locations)

    print('\n')
    print('\n')
    graph = graph.build_graph()
    print('The Graph implemenatation is:',graph)
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
    print("\r")
