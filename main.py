#!/usr/bin/env python3

from graph import UndirectedGraph


def main():
    graph = UndirectedGraph("graph.csv")
    print(graph.shortest_path('A', 'B'))
    print(graph.shortest_path('B', 'A'))
    print(graph.shortest_path('C', 'F'))
    print(graph.shortest_path('F', 'G'))
    print(graph.shortest_path('F', 'C'))
    print(graph.shortest_path('A', 'G'))
    print(graph.shortest_path('A', 'I'))


if __name__ == '__main__':
    main()
