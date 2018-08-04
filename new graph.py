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
        ("Vazhakulam", "Avoly", 2.3),
        ("Avoly","Vazhakulam",2.3),
        ("Vazhakulam", "Nadukara", 3.3),
        ("Vazhakulam", "Ayavana", 5.8),
        ("Nadukara", "Arakuzha", 2.9),
        ("Nadukara", "Vazhakulam",3.3),
        ("Arakuzha", "Perumballoor", 3.2),
        ("Arakuzha", "Nadukara", 2.9),
        ("Ayavana", "Anchapetty Jn", 3),
        ("Ayavana", "Varappetty", 7.7),
        ("Ayavana", "Vazhakulam",5.8),
        ("Perumballoor", "Arakuzha", 3.2),
        ("Anchapetty Jn", "Puthuppadi", 4.3),
        ("Anchapetty Jn", "Ayavana", 3),
        ("Anchapetty Jn", "Anicadu", 5.8),
        ("Puthuppadi", "Anchapetty Jn", 4.3),
        ("Puthuppadi", "Karukadam", 3.1),
        ("Puthuppadi", "Chalikkadavu", 3.9),
        ("Varappetty", "Karukadam", 2.2),
        ("Varappetty", "Mathirappilly", 2.3),
        ("Varappetty", "Kothamangalam", 5.4),
        ("Varappetty", "Ayavana", 7.7),
        ("Karukadam", "Mathirappilly", 2.2),
        ("Karukadam", "Varappetty", 2.2),
        ("Karukadam", "Puthuppadi", 3.1),
        ("Mathirappilly", "Kothamangalam", 4.1),
        ("Mathirappilly", "Karukadam", 2.2),
        ("Mathirappilly", "Varapetty", 2.3),
        ("Anicadu", "Anchapetty Jn", 5.8),
        ("Anicadu", "Chalikkadavu", 4.1),
        ("Kothamangalam", "Mathirappilly", 4.1),
        ("Kothamangalam", "Varappetty", 5.4),
        ("Chalikkadavu", "Kanam", 1.1),
        ("Chalikkadavu", "Puthuppadi", 3.9),
        ("Chalikkadavu", "Anicadu", 4.1),
        ("Kizhakkekara", "Kanam", 2.1),
        ("Kanam", "Chalikkadavu", 1.1),
        ("Kanam", "Kizhakkekara", 2.1)
    ]

#     print(edges)
    print(dijkstra(edges, "Avoly", "Kothamangalam"))
    rint(dijkstra(edges, "Kothamangalam", "Avoly"))