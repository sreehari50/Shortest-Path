import numpy as np
graph = {    'Vazhakulam': ['Avoly','Nadukara','Ayavana'],
             'Nadukara': ['Arakuzha','Vazhakulam'],
             'Arakuzha': ['Perumballoor','Nadukara'],
             'Perumballoor': ['Arakuzha'],
             'Avoly': ['Vazhakulam'],
             'Ayavana': ['Anchapetty Jn','Vazhakulam','Varappetty'],
             'Anchapetty Jn': ['Ayavana','Puthuppadi','Anicadu'],
             'Puthuppadi': ['Karukadam','Chalikkadavu','Anchapetty Jn'],
             'Varappetty': ['Karukadam','Mathirappilly','Kothamangalam','Ayavana'],
             'Karukadam': ['Mathirappilly','Varappetty','Puthuppadi'],
             'Mathirappilly': ['Karukadam','Varapetty','Kothamangalam'],
             'Kothamangalam': ['Mathirappilly','Varappetty'],
             'Anicadu': ['Chalikkadavu','Anchapetty Jn'],
             'Chalikkadavu': ['Kanam','Puthuppadi','Anicadu'],
             'Kizhakkekara': ['Kanam'],
             'Kanam':['Chalikkadavu']    
         }
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
print(find_shortest_path(graph, 'Avoly', 'Puthuppadi'))
