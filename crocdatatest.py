import csv
from collections import defaultdict
import sys
import math

filename ="CrocData.csv"
size = 100









class monitor():
    list_of_locations =[]
    edges_data = []

    import csv
    def __init__(self, size):
        self.dist = []
        self.list_of_locations = []
        self.edges_data = []
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
                            edgeb = line[6]
                            water = line[7]
                            gdist = line[8]
                            self.list_of_locations .append([nodenum, x, y, env, numsight, edgea, edgeb, water, gdist])
                            self.edges_data .append([edgea, edgeb])
                            if not nodenum in self.nodepoints:
                                self.nodepoints.append(nodenum)
                            index += 1
                            # print (index)
            
                            
        data.close


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
    
    # print (cm.list_of_locations)
    # print (cm.nodepoints)
    # user_location = input ("Enter your location")
    max_sight = max(cm.list_of_locations, key=lambda row: str(row[4]))
    print('\n')
    print('Previous max sighting')
    print('\nLocation:',max_sight[0],'number of Previous sightings:',max_sight[4])
    # print(max_sight)
    print('\n')
    graph = build_graph()
    print(graph)
