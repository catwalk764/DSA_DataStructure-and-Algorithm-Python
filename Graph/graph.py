#!/usr/bin/env python3

def add(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count =  node_count + 1
        nodes.append(v)
        for n in graph:
            n.append(0)
        temp = []
        for i in range(node_count):
            temp.append(0)
        graph.append(temp)

def add_edge(v1, v2,): #undirected and unweighted graph
    if v1 not in nodes:
        print(v1,"Is not present in the graph")
    elif v2 not in nodes:
        print(v2, "Is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = 1
        graph[index2][index1] = 1

def add_edge_w(v1, v2, w):# Weighted Graph
    if v1 not in nodes:
        print(v1, "Is not present in the graph")
    elif v2 not in nodes:
        print(v2, "Is not present in the graph")
    else:
        index1 = nodes.index(v1)
        index2 = nodes.index(v2)
        graph[index1][index2] = w
        graph[index2][index1] = w


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"), end=" ")
        print()



nodes = []
graph = []
node_count = 0

print("Before adding nodes")
print(nodes)
print(graph)
add("A")
add("B")
add("D")
add_edge("A", "E")
add_edge_w("A", "B", 20)
print("After adding nodes")
print(nodes)
print(graph)
print_graph()


