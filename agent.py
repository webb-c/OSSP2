import random
import numpy as np
import csv

class Agent():
    def __init__(self, method, num):
        self.method = method
        self.num = num
        self.csvfile = "results/csv/{}-{}.csv".format(self.method, self.num)
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

    def update_table(self):
    
    def print_table(self):
        for row in self.table:
            for v in row :
            print(v, end="\t")
        print()
        
    def save_table(self):
        csvfile = self.csvfile
        with open(csv_file_path, 'a+', newline='') as csvfile: 
            csv_writer = csv.writer(csvfile)
        for item in self.table:
            csv_writer.writerow([item])