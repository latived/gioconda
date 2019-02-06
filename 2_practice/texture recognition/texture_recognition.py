import matplotlib.pyplot as plt
import os
from skimage import io
from math import sqrt

class Node:
    def __init__(self, graylevel, posy, posx):
        self.graylevel = graylevel
        self.posy = posy
        self.posx = posx
        self.indegree = 0
        self.outdegree = 0
        self.activity = 0
        self.neighbors = []
        
def get_nodes_list(img):
    nodes = []
    width, height = img.shape
    
    for y in range(width):
        for x in range(height):
            nodes.append(Node(img[y][x], y, x))
    return nodes

def euclidian_distance(node1, node2):
    if isinstance(node1, Node) and isinstance(node2, Node):
        return (sqrt((node1.posx - node2.posx)**2 + (node1.posy - node2.posy)**2))    
    return 0

def create_relationships(nodes):
    for node in nodes:
        pass #TODO

def main():
    filepath = os.path.join("C:\\Users\pedro\Desktop\pasta", 'testeimg.jpg')

    img = io.imread(filepath)

    nodes = get_nodes_list(img)

    
main()
