import csv
from collections import defaultdict

import math

filename ="CrocData.csv"
size = 100



class monitor:
    list_of_locations =[]
    import csv
    def __init__(self, size):
        
        self.list_of_locations = []
        self.matrix = [[0 for x in range(size)]for y in range(size)]
        self.nodepoints=[]
        self.readData()


    def readData(self):    
        with open(filename,'r') as data:
                        csv_data_reader = csv.reader(data)
                        index = 0
                        next(csv_data_reader)
                        for line in csv_data_reader:
                            nodenum = line[0]
                            x = line[1]
                            y = line[2]
                            env = line[3]
                            numsight = line[4]
                            edge = line[5]
                            water = line[6]
                            gdist = line[7]
                            self.list_of_locations .append([nodenum, x, y, env, numsight, edge, water, gdist])
                            if not nodenum in self.nodepoints:
                                self.nodepoints.append(nodenum)
                            index += 1
                            

                            
        data.close






if __name__ == '__main__':
   
    cm=monitor(size) 
    print (cm.list_of_locations)
    print (cm.nodepoints)
