
def loadGraph(edgeFilename):
    adj = []
    max =-200000000
    with open(edgeFilename, "r") as f:
        graph = f.read().splitlines()
        for line in graph:
            x = line.split(" ")
            a = int(x[0])
            b = int(x[1])
            if a > max:
                max = a
            if b > max:
                max = b
        for i in range(0, max+1):
                adj.append([])
        for line in graph:
                x = line.split(" ")
                a = int(x[0])
                b = int(x[1])
                adj[a].append(b)
                adj[b].append(a)
    return adj

class MyQueue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"{self.items}"

    def enqueue(self, stuff):
        return self.items.append(stuff)

    def dequeue(self):
        return self.items.pop(0)

    def empty(self):
        return self.items == []

def BFS(G, s):
    queue = MyQueue()
    distance = []
    for u in range(0, len(G)):
        distance.append(float('inf'))
    distance[s] = 0
    queue.enqueue(s)
    while not queue.empty():
        u = queue.dequeue()

        for v in G[u]:
            if distance[v] == (float('inf')):
                distance[v] = distance[u]+1
                queue.enqueue(v)

    print(G, s, distance)
    return distance

def distanceDistribution(G):

    dict1 ={}
    percentages = []
    total =0
    for j in range(0, len(G)):
        distance = BFS(G, j)
        for i in range(0, len(distance)):
            if distance[i] in dict1.keys():
                tmp = dict1[distance[i]]
                tmp +=1
                dict1[distance[i]] = tmp
                total +=1
            else:
                dict1[distance[i]] =1
                total +=1
    for key in dict1.keys():
        percentages.append(str(key) + ":"+ str((round(dict1[key]/total*100, 2)))+'%')
    print("Total percentages:", percentages)

    return percentages

graph = loadGraph('edgesshort.txt')
# bigGraph = loadGraph('edges.txt')

distanceDistribution(graph)
# distanceDistribution(bigGraph)

