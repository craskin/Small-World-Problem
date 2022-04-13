import networkx as nx
import collections

def loadGraph(edgeFilename):
    list1 = []
    with open(edgeFilename, "r") as f:
        graph = f.read().splitlines()
        for line in graph:
            x = line.split(" ")
            a = int(x[0])
            b = int(x[1])
            combine = a, b
            list1.append(combine)
    return list1

class MyQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"{self.items}"

    def enqueue(self, stuff):
        return self.items.insert(0, stuff)

    def dequeue(self):
        return self.items.pop()

    def empty(self):
        return self.items == []

def BFS(G, s):
    queue = MyQueue()
    visited = []
    visited.append(s)
    queue.enqueue(s)
    while not queue.empty():
        m = queue.dequeue()
        for neighbor in G[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.enqueue(neighbor)
    print(visited)
    return visited

def distanceDistribution(G):
    graph = nx.Graph(G)
    distance = []
    dict1 = {}
    dict2 = dict(nx.all_pairs_shortest_path_length(graph))
    percentages = []
    numbers = []
    for node1 in dict2:
        for node2 in dict2[node1]:
            if dict2[node1][node2] > 0:
                distance.append(dict2[node1][node2])
    counter = collections.Counter()
    for i in distance:
        counter[i] += 1
    total = sum(counter.values())
    for num, count in sorted(counter.items()):
        numbers.append(num)
        print(str(round(count/total*100, 2))+"% of all distances are", num, "apart")
        percent = str(round(count/total*100,2))+"%"
        percentages.append(percent)
    for i in range(len(numbers)):
        dict1[numbers[i]] = percentages[i]
    print(dict1)
    return dict1

graph = loadGraph('edgesshort.txt')
bigGraph = loadGraph('edges.txt')
distanceDistribution(graph)
BFS(graph, 5)
BFS(graph, 13)
