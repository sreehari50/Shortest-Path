graph = {    'Vazhakulam': ['Ayavana','Nadukara','Avoly'],
             'Nadukara': ['Arakuzha','Vazhakulam'],
             'Arakuzha': ['Perumballoor','Nadukara'],
             'Perumballoor': ['Arakuzha'],
             'Avoly': ['Vazhakulam'],
             'Ayavana': ['Varappetty','Vazhakulam','Anchapetty Jn'],
             'Anchapetty Jn': ['Ayavana','Puthuppadi','Anicadu'],
             'Puthuppadi': ['Chalikkadavu','Anchapetty Jn','Karukadam'],
             'Varappetty': ['Mathirappilly','Ayavana','Karukadam'],
             'Karukadam': ['Mathirappilly','varappetty','Puthuppadi'],
             'Mathirappilly': ['Kothamangalam','Varapetty','Karukadam'],
             'Kothamangalam': ['Mathirappilly','Varappetty','Ayavana'],
             'Anicadu': ['Anchapetty Jn','Chalikkadavu'],
             'Chalikkadavu': ['Puthuppadi','Anicadu','Kanam'],
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
print(find_shortest_path(graph, 'Vazhakulam', 'Puthuppadi'))
