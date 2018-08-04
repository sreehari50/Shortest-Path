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
        ("Vazhakulam", "Nadukara", 6),
        ("Vazhakulam", "Ayavana", 11),
        ("Nadukara", "Arakuzha", 5),
        ("Nadukara", "Vazhakulam",6),
        ("Arakuzha", "Perumballoor", 4),
        ("Arakuzha", "Nadukara", 5),
        ("Ayavana", "Anchapetty Jn", 5),
        ("Ayavana", "Varappetty", 12),
        ("Ayavana", "Vazhakulam",11),
        ("Perumballoor", "Arakuzha", 4),
        ("Anchapetty Jn", "Puthuppadi", 7),
        ("Anchapetty Jn", "Ayavana", 5),
        ("Anchapetty Jn", "Anicadu", 13),
        ("Puthuppadi", "Anchapetty Jn", 7),
        ("Puthuppadi", "Karukadam", 4),
        ("Puthuppadi", "Chalikkadavu", 6),
        ("Varappetty", "Karukadam", 5),
        ("Varappetty", "Mathirappilly", 4),
        ("Varappetty", "Kothamangalam", 8),
        ("Varappetty", "Ayavana", 12),
        ("Karukadam", "Mathirappilly", 3),
        ("Karukadam", "Varappetty", 5),
        ("Karukadam", "Puthuppadi", 4),
        ("Mathirappilly", "Kothamangalam", 7),
        ("Mathirappilly", "Karukadam", 3),
        ("Mathirappilly", "Varapetty", 4),
        ("Anicadu", "Anchapetty Jn", 13),
        ("Anicadu", "Chalikkadavu", 7),
        ("Kothamangalam", "Mathirappilly", 7),
        ("Kothamangalam", "Varappetty", 8),
        ("Chalikkadavu", "Kanam", 2),
        ("Chalikkadavu", "Puthuppadi", 6),
        ("Chalikkadavu", "Anicadu", 7),
        ("Kizhakkekara", "Kanam", 4),
        ("Kanam", "Chalikkadavu", 2),
        ("Kanam", "Kizhakkekara", 4)
    ]

#     print(edges)
    print(dijkstra(edges, "Avoly", "Kothamangalam")[0]) #total time in minutes
    print(dijkstra(edges, "Avoly", "Kothamangalam")[1]) #path
#     print(dijkstra(edges, "Kothamangalam", "Avoly"))
