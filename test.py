#!C:\Users\lilia\AppData\Local\Programs\Python\Python310\python.exe

# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
import math
import random as rd
class Test:
    def __init__(self):
        self.data = np.zeros((10, 10))
        self.poids = 100
        self.index_debut = 0
        self.clous = []
        self.nb_clous = 0

    def set_clous(self):
        (n,m) = self.data.shape
        for i in range (n):
            self.clous.append([0,0])
            self.nb_clous +=7
            self.clous.append([0,5])
            self.clous.append([0,10])
            self.clous.append([5,10])
            self.clous.append([10,0])
            self.clous.append([10,5])
            self.clous.append([10,10])


    def data_random(self):
        (n,m) = self.data.shape
        for i in range(n):
            for j in range(m):
                self.data[i][j] = rd.randint(0, 255)
    
    def gray_line_calculator(self, debut, fin):

        x1, y1 = debut
        x2, y2 = fin

        #coefficient de la droite passant par les points début et fin (de la forme y = ax+b) 
        a = y2 - y1
        b = x1 - x2
        c = x1 * (y1 - y2) - y1 * (x1 - x2)

        #On refait une matrice de zéros
        gray_line = np.zeros(self.data.shape)

        #On calcule la valeur de gris de chaque pixels
        for i in range(int(min(x1,x2)), int(max(x1,x2))):
            for j in range(int(min(y1,y2)), int(max(y1,y2))):
                distance = abs(a * i + b * j - c) / math.sqrt(a**2 + b**2)
                gray_line[i,j]= self.scale_function(distance, self.poids)
        #print(gray_line)
        return gray_line
    
    def scale_function(self, x, poids):
        # Fonction qui permet de voir les lignes comme des nuances de gris
        if x < -1.5:
           return 0
        elif -1.5 < x < -0.5:
            return (x + 1.5) * poids
        elif -0.5 < x < 0.5:
            return 1 * poids
        elif 0.5 < x < 1.5:
            return (1.5 - x) * poids
        else:
            return 0
    
    def plot(self):
        plt.imshow(self.data, cmap='gray')
        plt.show()
        
    def generate(self):
        index = 0

        for i in range(3):
            for n in range(self.nb_clous):  
                print(str(i) + " " + str(n))
                grayline = self.gray_line_calculator(self.clous[index], self.clous[n])
                plt.imshow(grayline, cmap='gray')
                plt.show()
                
        


       
if __name__ == "__main__":
    test = Test()
    test.data_random()
    test.plot()
    test.set_clous()
    test.generate()

 