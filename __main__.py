import sys
import getopt
import time
import matplotlib.pyplot as plt
import numpy as np
from string_art_generator import StringArtGenerator

def main(argv):
    start_time = time.time()


    generator = StringArtGenerator()

    input_path = None
    input_fil = None
    input_clou = None

    default_path = "Images\Pomme.PNG"
    default_clou = 100
    default_fil = 100
    

    try:
       options, arguments = getopt.getopt(argv, "s:c:f:", ["string=", "clou=", "fil="])
    except getopt.GetoptError:
        print("Usage: script.py -s <string> -c <clou> -f <fil>")
        sys.exit(2)

    for option, value in options:
        if option in ("-s", "--string"):
            
            input_path = value

        if option in ("-c", "--clou"):
            
            input_clou = int(value)
            #print("input clou : " + str(input_clou))
            
            
        if option in ("-f", "--fil"):
            
            input_fil = int(value)
            #print(input_fil)


    if input_path is None:
        print("Default Path")
        generator.load_image(default_path)
    else: 
        try:
                
            generator.load_image("Images\\"+input_path)
            # print("Images\\"+input_path)
        except Exception as e:
            print(f"Une erreur s'est produite lors du chargement de l'image : {e}")
    
    generator.preprocess()

    if input_clou is None:
        print("Default Clous")
        generator.set_nb_clous(default_clou)
    else:
        try:
                
            generator.set_nb_clous(input_clou)
               
        except Exception as e:
                
            print(f"Une erreur s'est produite lors du chargement des clous : {e}")
    

    if input_fil is None:
        print("Default Fils")
        generator.set_nb_fil(default_fil)
    else:
        try:
                
            generator.set_nb_fil(input_fil)
               
        except Exception as e:
                
            print(f"Une erreur s'est produite lors du chargement des fils : {e}")

    generator.generate_v2_5()
    generator.rendu(str(input_path))
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main(sys.argv[1:])
