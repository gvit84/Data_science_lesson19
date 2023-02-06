#Task_1
import csv
import networkx as nx
import matplotlib.pyplot as plt

file = open("cities.csv", 'r')
list_of_cities = list(csv.reader(file, delimiter=";"))
file.close()
for i in list_of_cities:
    if type(i[2]) == str:
        i[2] = int(i[2])

G = nx.Graph()
G.add_weighted_edges_from(list_of_cities)
print(G)
nx.draw_networkx(G)
plt.show()


#Task_2
def find_min_route(graph, city_1, city_2):
    min_route = nx.dijkstra_path(graph, city_1, city_2)
    min_distance = nx.dijkstra_path_length(graph, city_1, city_2)
    return f"min route = {min_route} and min distance = {min_distance} km"


print(find_min_route(G, 'Lviv', 'Kyiv'))




