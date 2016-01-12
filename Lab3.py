
from sys import maxint
from random import randint
from time import time
import matplotlib.pyplot as plt

def getTime(func,connections,n):
    start = time()
    func(connections,n)
    end = time()
    return end - start


def floyd(connections, n):
    d = {0: connections}
    for a in range(1,n+1):
        d[a] = {}
        for b in range(1,n+1):
            for c in range(1,n+1):
                d[a][b,c] = min(d[a-1][b,c],d[a-1][b,a] + d[a-1][a,c])
    return d[n]

def dijkstra(connections,n):
    d = {2: connections}
    for i in range(2,n+1):
        d[i] = connections[1,i]
    candidates = [i+2 for i in range(n-1)]
    while len(candidates) != 0 :
        current = 0
        min = maxint
        for i in candidates:
            if min > d[i]:
                current = i
                min = d[i]
        for i in range(2,n+1):
            if (d[i] > d[current] + connections[current,i]) :
                d[i] = d[current] + connections[current,i]

        candidates.remove(current)
    return d[n]

def initGraph(n):
    connections = {}
    for i in range(1,n+1):
        connections[i,i] = 0
        for j in range(1,n+1):
            connections.setdefault((i,j), maxint)
    return connections

def generateGraph(n):
    connections = initGraph(n)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if(i != j):
                val = randint(1, n)
                if(val == 1):
                    connections[i,j] = 0
                else:
                    connections[i,j] = val
    return connections

vertices = []

times = [[],[]]

for n in range(4,40):
    g = generateGraph(n)
    vertices.append(n)
    times[0].append(getTime(floyd,g,n))
    times[1].append(getTime(dijkstra,g,n))

plt.plot(vertices,times[0],'r',label="Floyd")
plt.plot(vertices,times[1],'b',label="Dijkstra")
plt.legend()
plt.show()

