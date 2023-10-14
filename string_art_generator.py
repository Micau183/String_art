#!C:\Users\lilia\AppData\Local\Programs\Python\Python310\python.exe

from typing import Any
import numpy as np
import matplotlib.pyplot as plt
import math
import copy

from PIL import Image, ImageOps, ImageFilter, ImageEnhance

class StringArtGenerator:

    def __init__(self):

        #algo 1 et 2
        self.image = None
        self.data = None
        self.nb_clous = 0
        self.nb_fil = 0
        self.clous = []
        self.index_debut = 0
        self.pattern = []

        #algo 1 uniquement
        self.paths =[]
        self.weight = 20

        #algo 2 uniquement
        self.poids = 50
###-------------------------------###
### Partie commune aux deux algos ###
###-------------------------------###

    def set_nb_fil(self, nb_fil):
        self.nb_fil = nb_fil
        
    def set_nb_clous(self, nb_clous):
        self.nb_clous = nb_clous
        self.set_clous()
    
    def set_clous(self):
        angle = (2*math.pi)/self.nb_clous

        pas = range(self.nb_clous)
        

        rayon = self.get_rayon()
        
        x = [rayon + rayon*math.cos(t*angle) for t in pas]
        y = [rayon + rayon*math.sin(t*angle) for t in pas]
        
        self.clous = list(zip(x, y))
        #print(self.clous)
        #plt.figure(figsize=(8, 8))
        #plt.scatter(x, y, label='Données', color='black', marker='o')
        #plt.show()



    def load_image(self, path):
        self.image = Image.open(path)
    
    def show_image(self):
        plt.imshow(self.image)
        plt.show()
        #self.image.show()
    
    def get_rayon(self):
        
        return 0.5*np.min(np.shape(self.data))
    
    def preprocess(self):
        self.image = ImageOps.grayscale(self.image)
        self.image = ImageOps.invert(self.image)
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #self.image.show()

        self.image = ImageEnhance.Contrast(self.image).enhance(1)
        np_img = np.array(self.image)
        self.data = np.flipud(np_img).transpose()
        #self.image.show()

    def rendu(self, name):
        #print (self.paths)
        lines_x = []
        lines_y = []
        for i, j in zip(self.pattern, self.pattern[1:]):
            lines_x.append((i[0], j[0]))
            lines_y.append((i[1], j[1]))

        xmin = 0.
        ymin = 0.
        xmax = self.data.shape[0]
        ymax = self.data.shape[1]

        plt.ion()
        plt.figure(figsize=(5, 5))
        plt.axis('off')
        axes = plt.gca()
        axes.set_xlim([xmin, xmax])
        axes.set_ylim([ymin, ymax])
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)
        axes.set_aspect('equal')
        plt.draw()

        batchsize = 10
        for i in range(0, len(lines_x), batchsize):
            plt.plot(lines_x[i:i+batchsize], lines_y[i:i+batchsize],
                 linewidth=0.1, color='k')
        print(str(name) +"_"+str(self.nb_clous)+"_"+str(self.nb_fil) + "_v2.png")
        plt.savefig(str(name) +"_"+str(self.nb_clous)+"_"+str(self.nb_fil) + "_v2.png", bbox_inches='tight', pad_inches=0)
    
    ###---------------------------------------------------------------------------------###
    ###----------------------------------------Algo 1-----------------------------------###
    ###---------------------------------------------------------------------------------###
    def generate(self):
        self.calculate_paths()
        liste_de_fil = []
        delta = 0.0
        index_depart = 0
        datacopy = copy.deepcopy(self.data)
        for i in range(self.nb_fil):
            # calculate straight line to all other nodes and calculate
            # 'darkness' from start node

            # choose max darkness path
            darkest_index, darkest_path = self.choose_darkest_path(index_depart)

            # add chosen node to pattern
            liste_de_fil.append(self.clous[darkest_index])

            # substract chosen path from image
            self.data = self.data - self.weight*darkest_path
            self.data[self.data < 0.0] = 0.0

            # store current residual as delta for next iteration
            delta = np.sum(self.data)

            if (delta <= 0.0):
                print("Stopping iterations. No more data or residual unchanged.")
                break

            # continue from destination node as new start
            index_depart = darkest_index

        self.data = datacopy
        self.pattern = liste_de_fil

    def choose_darkest_path(self, index):
        max_darkness = -1.0
        for index, rowcol in enumerate(self.paths[index]):
            rows = [i[0] for i in rowcol]
            cols = [i[1] for i in rowcol]
            #Cela représente la somme des valeurs des pixels correspondants dans la matrice self.data pour le chemin actuel.
            darkness = float(np.sum(self.data[rows, cols]))

            if darkness > max_darkness:
                darkest_path = np.zeros(np.shape(self.data))
                darkest_path[rows,cols] = 1.0
                darkest_index = index
                max_darkness = darkness

        return darkest_index, darkest_path

    def calculate_paths(self):
        #Pour chaque clou on le prend lui et son index
        for index, clou_debut in enumerate(self.clous):
            #On ajoute une liste vide à paths
            self.paths.append([])
            #On calcul les chemin qui relie chaque clou à notre clou du début
            for clou_fin in self.clous:
                path = self.bresenham_path(clou_debut, clou_fin)
                #et on l'ajoute à la liste
                self.paths[index].append(path)

    def bresenham_path(self, start, end):

        """Bresenham's Line Algorithm"""

        # Setup initial conditions
        x1, y1 = start
        x2, y2 = end

        #vérification que les coords sont bien dans la matrice
        x1 = max(0, min(round(x1), self.data.shape[0]-1))
        y1 = max(0, min(round(y1), self.data.shape[1]-1))
        x2 = max(0, min(round(x2), self.data.shape[0]-1))
        y2 = max(0, min(round(y2), self.data.shape[1]-1))

        dx = x2 - x1
        dy = y2 - y1

        # Prepare output array
        path = []

        if (start == end):
            return path

        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)

        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Swap start and end points if necessary and store swap state
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1

        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1

        # Iterate over bounding box generating points between start and end
        y = y1
        for x in range(x1, x2 + 1):
            if is_steep:
                path.append([y, x])
            else:
                path.append([x, y])
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

        return path
    
    ###---------------------------------------------------------------------------------###
    ###----------------------------------------Algo 2-----------------------------------###
    ###---------------------------------------------------------------------------------###
    def generate_v2(self):

        erreur = np.sum(self.data)
        min_erreur = erreur
        index = self.index_debut
        next_index = 0
        liste_de_fil = []
        cpt = 0
        
        #print(self.nb_fil)
        for fil in range (self.nb_fil):
            
            
            if erreur < 5:
                break

            for i in range(int(self.nb_clous)):

                gray_line_matrice = self.gray_line_calculator(self.clous[index], self.clous[i])
                new_matrice = self.data - gray_line_matrice
                new_matrice[new_matrice < 0.0] = 0.0

                nouvelle_erreur = np.sum(new_matrice) 
                if (nouvelle_erreur < min_erreur ):
                    next_index = i
                    min_erreur = nouvelle_erreur
                    next_matrice = new_matrice
    


            erreur = min_erreur
            
            self.data = self.data - self.gray_line_calculator(self.clous[index], self.clous[next_index])
            
            self.data[self.data < 0.0] = 0.0
            index = next_index
            
            print(cpt, erreur)
            liste_de_fil.append(self.clous[index])
            cpt +=1
        self.pattern = liste_de_fil
    


    def gray_line_calculator(self, debut, fin):

        x1, y1 = debut
        x2, y2 = fin

        #coefficient de la droite passant par les points début et fin (de la forme y = ax+b) 
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1

        #On refait une matrice de zéros
        gray_line = np.zeros(self.data.shape)

        #On calcule la valeur de gris de chaque pixels
        for i in range(int(min(x1,x2)), int(max(x1,x2))):
            for j in range(int(min(y1,y2)), int(max(y1,y2))):
                distance = abs(a * i - j + b) / math.sqrt(a**2 + 1)
                gray_line[i,j]= self.scale_function(distance, self.poids)

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
        
    