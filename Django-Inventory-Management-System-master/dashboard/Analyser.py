from collections import deque
import random
from django.shortcuts import render
from django.http import HttpResponse
import logging
from ML.prediction import predict_traffic_level as predict_density

# #fournis par borispredict_density
# def predict_density(date_heure,hour,index):
#         status = random.choice([0, 1])
#         return status

#calcul de la densité des elements pour chaque chemin
def calculate_status_list(index_list,hour,date_heure):
        status_list = []
        for sublist in index_list:
            sublist_status = []
            for index in sublist:
                status =predict_density(date_heure,hour,index)
                sublist_status.append(status)
            status_list.append(sublist_status)
        return status_list

#calcul de la densité de traffic par chemin
def calculate_status_sum(status_list):
    sum_list = []
    for sublist in status_list:
        status_sum = sum(sublist)
        sum_list.append(status_sum)
    return sum_list

#pour obtenir la position correspondant au chemin de plus faible densité de traffic
def find_smallest_position(sum_list):
    smallest_value = min(sum_list)
    smallest_position = sum_list.index(smallest_value)
    return smallest_position

#pour obtenir une liste de position classé selon la densité du traffic sur un chemin
def sort_indexes_by_value(sum_list):
    indexes = list(range(len(sum_list)))
    indexes.sort(key=lambda i: sum_list[i])
    return indexes

#pour retourner les chemins dans l ordre de densité de traffic
def sort_lists_by_positions(positions, list_of_lists):
    sorted_list = [list_of_lists[pos] for pos in positions]
    return sorted_list

#revenir aux noms de carrefours
def convertir_liste_noms(liste_de_listes, correspondance):
    resultat = []
    for liste in liste_de_listes:
        nouvelle_liste = [correspondance[element] for element in liste]
        resultat.append(nouvelle_liste)
    return resultat

#ajout d element dans la liste de carrefour
def ajouter_carrefour(dictionnaire, nom_carrefour):
    nouvelle_cle = len(dictionnaire) 
    dictionnaire[nouvelle_cle] = nom_carrefour


def get_value(path):
    return next(iter(path.values()))

def calculate_traffic_stats(destination_list,depart_position,graphe,hour,date_heure):
    # Stocker tous les chemins entre deux destinations
    all_paths = []
    for i in range(len(destination_list)): 
            # print(graph)
            paths = graphe.find_paths(depart_position, destination_list[i]) 
            pathsWithDensityByCRossRoad=calculate_status_list(paths,hour,date_heure)
            pathsWithDensityByRoad=calculate_status_sum(pathsWithDensityByCRossRoad)
            # Trouver la position correspondant à l'itinéraire de plus faible densité de trafic
    
          
            smallest_density_road_position = find_smallest_position(pathsWithDensityByRoad)
            # sorted_positions = sort_indexes_by_value(pathsWithDensityByRoad)
            # sorted_lists = sort_lists_by_positions(paths, sorted_positions)
            # smallest_paths_with_Density={paths[smallest_density_road_position]:pathsWithDensityByRoad[smallest_density_road_position]}
            all_paths.append(paths[smallest_density_road_position])

    # sorted_paths = sorted(all_paths, key=get_value)
    # print(sorted_paths)
    # destination_order_list = [cle for dictionnaire in sorted_paths for cle in dictionnaire.keys()]
    return all_paths  

class Graph:
    def __init__(self):
        self.voisin = {}
        self.distances = {}

    def add_edge(self, edge_list):
        for edge in edge_list:
            u, v = edge
            if u not in self.voisin:
                self.voisin[u] = set()
            if v not in self.voisin:
                self.voisin[v] = set()
            self.voisin[u].add(v)
            self.voisin[v].add(u)
            
    def set_distances(self,node_from,node_to,distances):
        if node_from not in self.distances:
            self.distances[node_from] = {}
        self.distances[node_from][node_to] = distances

    def set_distances_Dict(self,distances_Dict):
        # for k,v in distances_Dict.items():
        #     self.distances[k] = v
        self.distances = distances_Dict

    def get_distances(self,node_from, node_to):
        if node_from in self.distances and node_to in self.distances[node_from]:
            return self.distances[node_from][node_to]
        else:
            return None
    
    def get_neighbors(self,node):
        return self.voisin[node]
    
    def find_paths(self, start, end):
        queue = deque([(start, [start])])
        paths = []

        while queue:
            node, current_path = queue.popleft()

            if node == end:
                paths.append(current_path)
            else:
                if node not in self.voisin:
                    continue

                neighbors = self.voisin[node]
                for neighbor in neighbors:
                    if neighbor not in current_path:
                        queue.append((neighbor, current_path + [neighbor]))

        return paths
    
    def best_path(self,PATH_LIST,distances):
        # TEMP = [] 
        # for i in range(1000):
        #     for path in PATH_LIST: 
        #         for node in path:
        #             if self.get_distances(node) < distances and path in PATH_LIST:
        #                # print(path)
        #                 PATH_LIST.remove(path)
        #                 #print(PATH_LIST)
        # return PATH_LIST
        
        best_paths = []
        best_score = float('inf')  # Initialiser le score avec une valeur positive infinie

        for path in PATH_LIST:
            total_distance = 0
            total_density = 0

            for i in range(len(path) - 1):
                node_from = path[i]
                node_to = path[i + 1]

                # Obtenir la distance entre les nœuds
                distance = self.get_distances(node_from, node_to)

                # Obtenir la densité de trafic prédite
                density = predict_density(node_to)

                total_distance += distance
                total_density += density

            # Calculer le score en tenant compte de la distance et de la densité de trafic
            score = total_distance * 0.65 + total_density *0.35
            # Mettre à jour le chemin optimal si le score actuel est meilleur que le meilleur score précédent
            if score < best_score:
                best_paths = [path]
                best_score = score
            elif score == best_score:
                best_paths.append(path)

        return best_paths
        


carrefours = {
    1: "Carrefour obili",
    2: "Carrefour biyem-assi",
    3: "Carrefour melen",
    4: "Carrefour simbock",
    5: "Carrefour etoug ebe",
    6: "Carrefur mvog bi",
    7: "Carrefour mvan",
    8: "carrefour odza",
    9: "carrefour mvog-ada",
    # 8: "Carrefour etoa-meki",
    # 9: "Carrefour coron",
    10: "Carrefour awae",
    #11: "Carrefour odza",
    #12: "Carrefour golf",
    #13: "Carrefour mvan",
    #14: "Carrefour ekoudoum",
    #15: "Carrefour nkomo",
    #16: "Carrefour eig-edzoa",
    #17: "Carrefour carriere",
    #18: "Carrefour efoulan",
    #19: "Carrefour nkoabang",
    #20: "Carrefour emana",
    #21: "Carrefour essomba",
    #22: "Carrefour sous-manguier",
    #23: "Carrefour miniferme",
    #24: "Carrefour otou",
    #25: "Carrefour dallas",
    #26: "Carrefour nkoabang",
    #27: "Carrefour etoa-meki",
    #28: "Carrefour carriere",
    #29: "Carrefour ekounou",
    #30: "Carrefour gros bouquet"
}

graph = Graph()

#distanc en km
distances_dict = {
    1: {2:1.2, 3:1.4, 4:4.0},
    2: {1:1.2, 4:2.9, 5:2, 6:5.8},
    3: {1:1.4, 9:5.8},
    4: {1:4.0, 2:2.9, 5:3.9},
    5: {2:2, 4:2.9},
    6:{9:2.1, 2:5.8, 10:4.9, 7:3.5},
    7: {8:4.0, 10:5.6, 6:3.5},
    8:{10:6.6, 7:4.0},
    9:  {3:5.8, 6:2.1},
    10: {8:6.6, 6:4.9, 7:5.6},
}

# # Add edges to the graph
edges = [
    [1, 2],
    [1, 3],
    [1, 4],
    [2, 4],
    [2, 5],
    [2, 6],
    [4, 5],
    [6, 7],
    [6, 2],
    [6, 9],
    [6, 10],
    [7, 8],
    [7,10],
    [8,10],
    [9,3],
]

graph.add_edge(edges)
graph.set_distances_Dict(distances_dict)


    
# liste_de_listes = [[1, 3, 4, 5], [1, 2, 4, 5], [1, 3, 2, 4, 5], [1, 2, 3, 4, 5]]
# paths = graph.find_paths('A', 'E')


def traitement_formulaire(request):
    if request.method == 'POST':
        lieu_depart =int( request.POST.get('lieu-depart'))
        destination = request.POST.get('destination')
        heure_depart = request.POST.get('heure-depart')
        date = request.POST.get('date')
        date_heure = date+" "+heure_depart + ":00"
        heure_dep = heure_depart.split(":")[0]
        print(heure_dep)
        
        if(lieu_depart!=destination):

            dest=[int(destination)]

            destination_order_list=calculate_traffic_stats(dest,lieu_depart,graph,heure_dep,date_heure)
            destname=convertir_liste_noms(destination_order_list,carrefours)
            print(destname)
    return HttpResponse(f"Itineraire à suivre : ! {destname}")

