from collections import defaultdict
from heapq import *

def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))

    q, seen, mins = [(0,f,())], set(), {f: 0}
    while q:
        (cost,v1,path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t: return (cost, path)

            for c, v2 in g.get(v1, ()):
                if v2 in seen: continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")

if __name__ == "__main__":
    edges = [
        ("Vazhakulam", "Avoly", 4),
        ("Avoly","Vazhakulam",4),
        ("Avoly","Anicadu",5),
        ("Anicadu","Avoly",5),
        ("Anicadu","Kizhakkekara",5),
        ("Kizhakkekara", "Anicadu", 5),
        ("Kizhakkekara", "Muvattupuzha", 8),
        ("Muvattupuzha", "Kizhakkekara", 8),
        ("Arakuzha", "Perumballoor", 4),
        ("Perumballoor", "Arakuzha", 4),
        ("Perumballoor", "Muvattupuzha", 10),
        ("Muvattupuzha", "Perumballoor", 10),
        ("Kothamangalam", "Karukadam", 12),
        ("Karukadam", "Kothamangalam",12),
        ("Karukadam", "Puthuppady", 5),
        ("Puthuppady", "Karukadam", 5),
        ("Puthuppady", "Muvattupuzha", 9),
        ("Muvattupuzha", "Puthuppady", 9)
    ]

#     print(edges)
    print(dijkstra(edges, "Vazhakulam", "Kothamangalam")[0]) #total time in minutes
    print(dijkstra(edges, "Kothamangalam", "Vazhakulam")[0]) #path
