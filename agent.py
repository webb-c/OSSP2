import random
import numpy as np
import csv

class Agent():
    def __init__(self, method, num):
        self.method = method
        self.num = num
        if self.num == -1 :
            self.csv_path = "results/csv/n-step TD/{}.csv".format(self.method)
        else :
            self.csv_path = "results/csv/{}/{}.csv".format(self.method, self.num)
        self.table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def select_action(self):
        coin = random.random()
        if coin < 0.25:
            action = 0
        elif coin < 0.5:
            action = 1
        elif coin < 0.75:
            action = 2
        else:
            action = 3
        return action

    def get_table(self):
        return self.table
    
    def set_table(self, table):
        self.table = table
    
    def print_table(self):
        for row in self.table:
            for v in row :
                print(round(v, 3), end="\t")
            print()
        
    def save_table(self):
        flat_data = [item for sublist in self.table for item in sublist]
        with open(self.csv_path, 'a+', newline='') as csv_file: 
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(flat_data)
    
    def reset(self):
        self.table = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]