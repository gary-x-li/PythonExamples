#!/usr/bin/env python3

n = int(input())
g = []
b = []
for i in range(n):
    g.append(int(input()))
    b.append(int(input()))

graphs = []
for i in range(n):
    graphs.append({g[i], b[i]})
 
