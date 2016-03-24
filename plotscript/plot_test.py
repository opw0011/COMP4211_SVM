#!python
"""
Usage:

    python plot_test.py [testfile] [prediction] [figurefile]
        - plot the data from [testfile], using the class in [prediction] 
        save the figure in [figurefile]. 
"""



import numpy as np
import matplotlib.pyplot as plt
import sys 


if __name__ == "__main__":


    def read_data(filename):
        with open(filename, "rb") as f:
            lines = np.array([map(lambda x: float(x.split(':')[-1]), line.strip().split(' ')) for line in f])
        return lines

    def read_label(filename):
        with open(filename, "rb") as f:
            lines = np.array([map(lambda x: float(x), line.strip().split(' ')) for line in f])
            lines = lines.flatten()
        return lines



    def plot_data(data, label):
        cls_all = np.unique(label)
        markers = ['d', '*']
        colors = ['b', 'g']
        for i, cls in enumerate(cls_all):
            d =  data[label == cls, -2:]
            plt.scatter(d[:,0], d[:,1], marker = markers[i], facecolors = 'none', edgecolors = colors[i])
        plt.legend(['class 1', 'class 2'])


    lines = read_data(sys.argv[1])
    label = read_label(sys.argv[2])
    plot_data(lines, label)
    

    savename = sys.argv[-1].split('.')[0]+'.png'
    
    plt.savefig(savename, dpi = 240)
    




   
