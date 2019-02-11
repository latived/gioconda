import matplotlib.pyplot as plt
from skimage import io
from math import sqrt
import numpy as np
import os
import copy
import random

class Node:
    def __init__(self, graylevel, posy, posx):
        self.graylevel = graylevel
        self.posy = posy
        self.posx = posx
        self.indegree = 0
        self.outdegree = 0
        self.activity = 0
        self.neighbors = []

    def __repr__(self):
        return "|NODE[" + str(self.posy) + "]" + "[" + str(self.posx) + "] = " + str(self.activity) + "|"

def get_nodes_list(img, nodes):
    #Mapping the pixels of the image into a list of nodes, where each node store the gray level of the pixel and the (X, Y) position 
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
    #Creating links between the 'node' and all nodes in the possible links area, based on euclidian distances less or igual to given radius
    for y in range(begin_y, end_y + 1):
        for x in range(begin_x, end_x + 1):
            if node != nodes_matrix[y][x] and euclidian_distance(node, nodes_matrix[y][x]) <= radius:
                link_intensity = int(node.graylevel) - int(nodes_matrix[y][x].graylevel)

                #Links with negative intensity are discarded
                if link_intensity > 0:
                    create_link(node, nodes_matrix[y][x], link_intensity)

def create_dnetwork(nodes_matrix, matrix_width, matrix_height, radius):
    #Calculating the area of possible connections with 'node'
    for line in nodes_matrix:
        for node in line:
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
                if neighbor[1] > threshold:
                    node.outdegree -= 1
                    neighbor[0].indegree -= 1
                    node.neighbors.remove(neighbor)

def get_node_by_weight(links_list):
    total_weight = 0
    current_weight = 0

    for link in links_list:
        current_weight = link[1]
        random_number = random.randint(0, total_weight + current_weight)

        if random_number >= total_weight:
            selected = link[0]

        total_weight += current_weight

    return selected

def random_walks(network, number_of_walks, max_walk_length):
    for line in network:
        for node in line:
            #The walker starts at each node of the network 'number_of_walks' times
            if node.outdegree > 0:
                for i in range(number_of_walks):
                    current_node = node
                    for j in range(max_walk_length):
                        #If there's no outgoing link the walker stops
                        if current_node.outdegree > 0:
                            current_node = get_node_by_weight(current_node.neighbors)
                            current_node.activity += 1
                        else:
                            break

def main():
    #Defining the path of the image file
    filepath = os.path.join("C:\\Users\\pedro\\Documents\\UFAL\\Pesquisa\\Codigos\\gioconda\\2_practice\\texture recognition\\img", 'testeimg.jpg')
    
    #Loading image data
    img = io.imread(filepath)
    img_width, img_height = img.shape

    differents_radius = [2]
    thresholds = [10]    

    #Number of walks started at each node
    number_of_walks = 25
    #Maximum number of nodes visited at each walk
    max_walk_length = 500

    nodes = []
    feature_vector = []

    get_nodes_list(img, nodes)
    
    #Reshape the list of nodes into a matrix with the same shape of the image
    initial_nodes_matrix = np.array(nodes).reshape(img_width, img_height)
    
    for radius_of_connection in differents_radius:
        #Copy of the original matrix of nodes to apply a specific radius
        nodes_matrix = copy.deepcopy(initial_nodes_matrix)
        
        #Create the base directed network with radius 'radius_of_connection'
        create_dnetwork(nodes_matrix, img_width, img_height, radius_of_connection)

        #Save the initial network to apply differents thresholds
        initial_radius_network = copy.deepcopy(nodes_matrix)


        for threshold in thresholds:

            current_network = copy.deepcopy(initial_radius_network)
        
            #Links are removed based on a threshold, if link intensity > threshold, the link will be discarded
            filter_links_by_threshold(current_network, threshold)
            
            #Estimate the activity of the nodes by random walks started at each node 
            random_walks(current_network, number_of_walks, max_walk_length)

            #Feature vector with all networks with different radius and thresholds
            feature_vector.append((radius_of_connection, threshold, copy.deepcopy(current_network)))

main()















