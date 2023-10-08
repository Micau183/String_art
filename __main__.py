import sys
import getopt
import cProfile
import pstats
import matplotlib.pyplot as plt
import numpy as np
from string_art_generator import StringArtGenerator


def main(argv):
    generator = StringArtGenerator()
    input_path = None
    default_path = "Images\Pomme.PNG"

    try:
        options, arguments = getopt.getopt(argv, "s:", ["string="])
    except getopt.GetoptError:
        print("Usage: script.py -s "+default_path)
        sys.exit(2)

    for option, value in options:
        if option in ("-s", "--string"):
            
            input_path = value
            
            try:
                
                generator.load_image("Images\\"+input_path)
                # print("Images\\"+input_path)
            except Exception as e:
               print(f"Une erreur s'est produite lors du chargement de l'image : {e}")

    if input_path is None:
        print("Default Path")
        generator.load_image(default_path)

    generator.preprocess()
    generator.set_nb_clous(500)
    generator.set_nb_fil(2100)
    pattern = generator.generate()
    

    lines_x = []
    lines_y = []
    for i, j in zip(pattern, pattern[1:]):
        lines_x.append((i[0], j[0]))
        lines_y.append((i[1], j[1]))

    xmin = 0.
    ymin = 0.
    xmax = generator.data.shape[0]
    ymax = generator.data.shape[1]

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
        plt.draw()
        plt.pause(0.000001)
    a = str(np.random.randint(0, 10000))
    print(a)
    plt.savefig(input_path +a+'.png', bbox_inches='tight', pad_inches=0)

    

    

if __name__ == "__main__":
    main(sys.argv[1:])