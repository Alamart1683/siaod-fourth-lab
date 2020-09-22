# Список импортов
from Graph import Graph
from Interface import Interface
import networkx as nx
import matplotlib.pyplot as plt
import pylab as pl

# Консольное меню программы
menu = Interface()
# Вызов метода отображения главного меню
menu.interface_Main()

# Цикл обработки команд
while True:
    # Ввод выбранного действия
    Step = menu.input_Controller()

    # Задание 1
    if Step == 1:
        print("")
        # Объекта класса графа
        task1 = Graph(100, 1)
        # Цикл обхода графа и его поэтапной отрисовки
        pl.ion()
        pl.show()
        for vertex in range(task1.user_value):
            pl.clf()
            task1.anonymous_find(vertex)
            color_list = task1.append_color_for_vertex(vertex)
            nx.draw_kamada_kawai(task1.graph, node_size = 275, node_color = color_list, 
            edge_color = "black", font_color = "black", font_weight = 5, with_labels = True)
            pl.show()
            pl.pause(1.0)
        menu.interface_Main()

    # Задание 2
    elif Step == 2:
        print("")
        # Объекта класса графа
        task2 = Graph(100, 2)
        # Цикл обхода графа и его поэтапной отрисовки
        pl.ion()
        pl.show()
        for vertex in range(task2.user_value):
            pl.clf()
            task2.anonymous_find(vertex)
            color_list = task2.append_color_for_vertex(vertex)
            nx.draw_kamada_kawai(task2.graph, node_size = 275, node_color = color_list, 
            edge_color = "black", font_color = "black", font_weight = 5, backgrond_color = "beige", with_labels = True)
            pl.show()
            pl.pause(1.0)
        menu.interface_Main()
       
    # Задание 3
    elif Step == 3:
        print("")
        # Объекта класса графа
        task3 = Graph(100, 3)
        # Цикл обхода графа и его поэтапной отрисовки
        pl.ion()
        pl.show()
        for vertex in range(task3.user_value):
            pl.clf()
            task3.anonymous_find(vertex)
            color_list = task3.append_color_for_vertex(vertex)
            nx.draw_kamada_kawai(task3.graph, node_size = 275, node_color = color_list, 
            edge_color = "black", font_color = "black", font_weight = 5, with_labels = True, )
            pl.show()
            pl.pause(1.0)
        menu.interface_Main()

    # Задание 4
    elif Step == 4:
        print("")
        # Объекта класса графа
        task4 = Graph(100, 4)
        # Цикл обхода графа и его поэтапной отрисовки
        pl.ion()
        pl.show()
        for vertex in range(task4.user_value):
            pl.clf()
            task4.anonymous_find(vertex)
            color_list = task4.append_color_for_vertex(vertex)
            nx.draw_kamada_kawai(task4.graph, node_size = 275, node_color = color_list, 
            edge_color = "black", font_color = "black", font_weight = 5, with_labels = True)
            pl.show()
            pl.pause(1.0)
        menu.interface_Main()

    # Выход из программы
    elif Step == 5:
        print("Программа завершена")
        break

    # Остальные случаи
    else:
        print("Ошибка ввода")
        print("")

