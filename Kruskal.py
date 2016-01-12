from random import randint
from time import time
import matplotlib.pyplot as plt

class edge:
    fr = 1
    to = 1
    cost = 0
    def __init__(self, fr, to, cost):
        self.fr = fr
        self.to = to
        self.cost = cost
class graph:
    def __init__(self,n,data):
        self.n = n
        self.data = data
        self.data.sort(key=lambda x: x.cost) #sort list of edges by cost . Greedy approach :)

    def getElement(self,a,b):
        return self.data[a][b]



def positionInArray(arr, el):
    pos = 0
    for i in arr:
        if i == el:
            return pos
        pos+=1
    return -1

def existsInArray(arr,el):
    return positionInArray(arr,el) != -1

def insertInArray(arr, el):
    for i in arr:
        if i == el:
            return
    arr.append(el)

def getTime(func,graph):
    start = time()
    func(graph)
    end = time()
    return end-start

def randomGraph(n, edges):
    data = []
    connected = []
    unconnected = [i+1 for i in range(n)]
    for i in range(edges):
        startingVertex = 0
        endingVertex = 0
        cost = randint(1,10)
        if(len(unconnected) != 0):
            startingVertex = unconnected.pop(0)
            endingVertex = 0
            if(len(connected) == 0):
                startingVertex = unconnected.pop(0)
            else:
                endingVertex = connected[randint(0,len(connected)-1)]
        else:
            startingVertex = randint(1,n)
            endingVertex = randint(1,n)
            while endingVertex == startingVertex:
                endingVertex = randint(1,n)

        insertInArray(connected, endingVertex)
        insertInArray(connected, startingVertex)
        data.append(edge(startingVertex,endingVertex,cost))
    return graph(n,data)


def kruskal(graph):
    connectedVerticies = []
    selectedEdges = []
    i = 0
    while (len(connectedVerticies) != graph.n) and (i < len(graph.data)):
        e = graph.data[i]
        a = not(existsInArray(connectedVerticies, e.fr))
        b = not(positionInArray(connectedVerticies, e.to))
        if (a != b) or len(connectedVerticies) == 0:
            insertInArray(connectedVerticies, e.fr)
            insertInArray(connectedVerticies, e.to)
            selectedEdges.append(e)
        i += 1
    return selectedEdges

def prim(graph):
    selectedEdges = []
    connectedVerticies = [1]
    while len(connectedVerticies) != graph.n:
        for e in graph.data:
            aPosition = positionInArray(connectedVerticies, e.fr)
            bPosition = positionInArray(connectedVerticies, e.to)
            if ((aPosition == -1 and bPosition != -1)) or (bPosition == -1 and aPosition != -1):
                if aPosition == -1:
                    connectedVerticies.append(e.fr)
                else:
                    connectedVerticies.append(e.to)
                selectedEdges.append(e)
                graph.data.remove(e)
                break

    return selectedEdges

colors = ['r','g','b','y']

def plotDensity(n):
    xAxis = []
    primArr = []
    kruskalArr = []
    for i in range(10,90):
        g = randomGraph(i, i * (i - n))
        primArr.append(getTime(prim,g))
        kruskalArr.append(getTime(kruskal,g))
        xAxis.append(g.n)

    plt.plot(xAxis, primArr, colors.pop(0), label="Prim d="+str(n))
    plt.plot(xAxis, kruskalArr, colors.pop(0), label="Kruskal d="+str(n))

plotDensity(4)
plotDensity(0)

plt.legend()
plt.show()