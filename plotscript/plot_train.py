#!python
"""
Usage:
    python plot_train.py [trainfile] [figurefile]
        - plot the data from [trainfile], save the figure in [figurefile]

    python plot_train.py [trainfile] [modelfile] [figurefile]
        - plot the data from [trainfile], highlight the support vectors in [modelfile],
        save the figure in [figurefile]. Note: In [modelfile], you should remove all
        other things except support vectors

"""



import numpy as np
import matplotlib.pyplot as plt
import sys 


if __name__ == "__main__":


    def read_data(filename):
        with open(filename, "rb") as f:
            lines = np.array([map(lambda x: float(x.split(':')[-1]), line.strip().split(' ')) for line in f])
        return lines

    def plot_data(data):
        cls_all = np.unique(data[:, 0])
        markers = ['d', '*']
        colors = ['b', 'g']
        for i, cls in enumerate(cls_all):
            d =  data[data[:,0] == cls, 1:]
            plt.scatter(d[:,0], d[:,1], marker = markers[i], facecolors = 'none', edgecolors = colors[i])
        plt.legend(['class 1', 'class 2'])

    def plot_sv(data):
        d = data[:, 1:]
        sca = plt.scatter(d[:,0], d[:,1],s = 60, marker = 'o', facecolors = 'none', edgecolors = 'r')
        plt.legend(['class 1', 'class 2', 'support vector'])



    lines = read_data(sys.argv[1])
    plot_data(lines)

    
    if len(sys.argv) == 4:
        sv = read_data(sys.argv[2])
        plot_sv(sv)
    

    savename = sys.argv[-1].split('.')[0]+'.png'
    
    plt.savefig(savename, dpi = 240)
    




   
