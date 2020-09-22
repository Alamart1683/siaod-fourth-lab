# Список импортов
import random
import networkx as nx
import numpy as np

# Класс графа
class Graph:
    # Конструктор
    def __init__(self, user_value, count):
        self.user_value = user_value
        self.anonymous_legion = []
        self.count = count
        self.graph = nx.Graph()
        # Цикл добавления вершин в социальный граф
        for vertex in range(self.user_value):
            self.graph.add_node(vertex)
        # Цикл создания связей между вершинами
        for vertex in range(self.user_value):
            neighbors = len([self.graph.neighbors(vertex)])
            if neighbors < 4:
                edges = random.randint(1, 4 - neighbors)
                # Цикл создания связей
                while edges > 0:
                    neighbor = random.randint(0, self.user_value - 1)
                    if neighbor != vertex or len(list(self.graph.neighbors(neighbor))) <= 3:
                        self.graph.add_edge(vertex, neighbor)
                        edges = edges - 1

    # Метод поиска незнакомцев с определенным количеством общих знакомых
    def anonymous_find(self, current_user):
        friendly_users = list(self.graph.neighbors(current_user))
        # Цикл обхода всех вершин графа
        for vertex in range(self.user_value):
            if vertex != current_user and vertex not in friendly_users:
                number = 0
                current_friendly_list = list(self.graph.neighbors(vertex))
                # Цикл обхода ребер графа (друзей пользователя)
                for jertex in friendly_users:
                    if jertex in current_friendly_list:
                        number = number + 1
                if number == self.count:
                    self.anonymous_legion.append(vertex)

    # Метод придания искомым вершинам цветовой окраски
    def append_color_for_vertex(self, current_user):
        friendly_users = list(self.graph.neighbors(current_user))
        colour_list = []
        # Цикл придания цвета
        for index in range(self.user_value):
            colour_list.append("magenta")
            index = index + 1
        # Цикл разукрашивания анонимусов
        for anonymous in self.anonymous_legion:
            colour_list[anonymous] = "yellow"
        # Цикл разукрашивания друзей
        for friendly_user in friendly_users:
            colour_list[friendly_user] = "orange"
        colour_list[current_user] = "red"
        self.anonymous_legion = []
        return colour_list