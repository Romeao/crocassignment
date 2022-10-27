from ast import Num
import csv
from collections import defaultdict
import sys
import math

filename ="CrocData.csv"
size = 100


class monitor():
    list_of_locations =[]
    edges_data = []
    num_of_sightings = []

    import csv
    def __init__(self, size):
        self.distance_data = []
        self.list_of_locations = []
        self.edges_data = []
        num_of_sightings= []
        self.matrix = [[0 for x in range(size)]for y in range(size)]
        self.nodepoints=[]
        self.readData()


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
                            self.num_of_sightings .append([numsight])
                            if not nodenum in self.nodepoints:
                                self.nodepoints.append(nodenum)
                            index += 1
                            # print (index)
            
                            
        data.close

class graph:

    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)


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
    print("The list printed sorting in descending order: ")
    if cm.num_of_sightings !="":
        print(sorted(cm.num_of_sightings, key=lambda i: ',', reverse=True))
