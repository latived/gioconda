import matplotlib.pyplot as plt
from skimage import io
from math import sqrt
import numpy as np
import os

class Node:
    def __init__(self, graylevel, posy, posx):
        self.graylevel = graylevel
        self.posy = posy
        self.posx = posx
        self.indegree = 0
        self.outdegree = 0
        self.activity = 0
        self.neighbors = []
        
def get_nodes_list(img, nodes):
    width, height = img.shape
    
    for y in range(width):
        for x in range(height):
            nodes.append(Node(img[y][x], y, x))

def euclidian_distance(node1, node2):
    if isinstance(node1, Node) and isinstance(node2, Node):
        return (sqrt((node1.posx - node2.posx)**2 + (node1.posy - node2.posy)**2))    
    return 0

def create_link(node_tail, node_head):
    node_tail.neighbors.append((node_head, int(node_tail.graylevel) - int(node_head.graylevel)))
    node_head.indegree += 1
    node_tail.outdegree += 1

    
def create_links_area(node, nodes_matrix, radius, begin_y, end_y, begin_x, end_x):
    for y in range(begin_y, end_y + 1):
        for x in range(begin_x, end_x + 1):
            if node != nodes_matrix[y][x] and euclidian_distance(node, nodes_matrix[y][x]) <= radius:
                create_link(node, nodes_matrix[y][x])

def create_dnetwork(nodes_matrix, matrix_width, matrix_height, radius):
    for line in nodes_matrix:
        for node in line:
            #Calculating the area of possible connections with 'node'
            begin_y = node.posy - radius
            if begin_y < 0:
                begin_y = 0

            end_y = node.posy + radius
            if end_y >= matrix_height:
                end_y = matrix_height - 1
                
            begin_x = node.posx - radius
            if begin_x < 0:
                begin_x = 0

            end_x = node.posx + radius
            if end_x >= matrix_width:
                end_x = matrix_width - 1

            create_links_area(node, nodes_matrix, radius, begin_y, end_y, begin_x, end_x)
            

def main():
    filepath = os.path.join("C:\\Users\\pedro\\Documents\\UFAL\\Pesquisa\\Codigos\\gioconda\\2_practice\\texture recognition\\img", 'testeimg.jpg')
    
    img = io.imread(filepath)
    img_width, img_height = img.shape

    nodes = []

    get_nodes_list(img, nodes)
    
    nodes_matrix = np.array(nodes).reshape(img_width, img_height)

    radius_of_connection = int(input("Enter the radius of connection: "))

    threshold = int(input("Enter the threshold: "))
    
    create_dnetwork(nodes_matrix, img_width, img_height, radius_of_connection)
    
main()
