import matplotlib.pyplot as plt
from skimage import io
from math import sqrt
import numpy as np
import os
import copy

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
    #mapping the pixels of the image into a list of nodes, where each node store the gray level of the pixel and the (X, Y) position 
    width, height = img.shape
    
    for y in range(width):
        for x in range(height):
            nodes.append(Node(img[y][x], y, x))

def euclidian_distance(node1, node2):
    if isinstance(node1, Node) and isinstance(node2, Node):
        return (sqrt((node1.posx - node2.posx)**2 + (node1.posy - node2.posy)**2))    

    return 0

def create_link(node_tail, node_head, intensity):
    node_tail.neighbors.append((node_head, intensity))
    node_head.indegree += 1
    node_tail.outdegree += 1

    
def create_links_area(node, nodes_matrix, radius, begin_y, end_y, begin_x, end_x):
    #creating links between the 'node' and all nodes in the possible links area, based on euclidian distances less or igual to given radius
    for y in range(begin_y, end_y + 1):
        for x in range(begin_x, end_x + 1):
            if node != nodes_matrix[y][x] and euclidian_distance(node, nodes_matrix[y][x]) <= radius:
                link_intensity = int(node.graylevel) - int(nodes_matrix[y][x].graylevel)

                #links with negative intensity are discarded
                if link_intensity > 0:
                    create_link(node, nodes_matrix[y][x], link_intensity)

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
            
def filter_links_by_threshold(nodes_matrix, threshold):
    for line in nodes_matrix:
        for node in line:
            for neighbor in node.neighbors:
                if neighbor[1] >= threshold:
                    node.outdegree -= 1
                    neighbor[0].indegree -= 1
                    node.neighbors.remove(neighbor)

def main():
    filepath = os.path.join("C:\\Users\\pedro\\Documents\\UFAL\\Pesquisa\\Codigos\\gioconda\\2_practice\\texture recognition\\img", 'testeimg.jpg')
    
    img = io.imread(filepath)
    img_width, img_height = img.shape

    nodes = []

    get_nodes_list(img, nodes)
    
    #reshape the list of nodes into a matrix with the same shape of the image
    initial_nodes_matrix = np.array(nodes).reshape(img_width, img_height)
    
    differents_radius = [2, 5, 8]

    feature_vector = []

    for radius_of_connection in differents_radius:

        #Copy of the original matrix of nodes to apply a specific radius
        nodes_matrix = copy.deepcopy(initial_nodes_matrix)
        
        #create the base directed network with radius 'radius_of_connection'
        create_dnetwork(nodes_matrix, img_width, img_height, radius_of_connection)

        #save the initial network to apply differents thresholds
        initial_radius_network = copy.deepcopy(nodes_matrix)

        thresholds = [10, 50, 100]
        
        for threshold in thresholds:
            current_network = copy.deepcopy(initial_radius_network)
        
            filter_links_by_threshold(current_network, threshold)


            
            #TODO random walks step




            #feature vector with all networks with different radius and thresholds
            feature_vector.append((radius_of_connection, threshold, copy.deepcopy(current_network)))

    print(feature_vector)
main()















