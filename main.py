#!/usr/bin/env python3

from graph import UndirectedGraph


def main():
    graph_filename = input("Graph filename: ")
    graph = UndirectedGraph(graph_filename)

    start_node = input("Start node: ")
    end_node = input("End node: ")

    shortest_path = graph.shortest_path(start_node, end_node)
    path = shortest_path['path']
    cost = shortest_path['cost']

    if path is None:
        print(f"There is no path connecting {start_node} to {end_node}.")
    else:
        print(f"Path from {start_node} to {end_node} is {path_to_string(path)},",
              f"and have cost {cost}.")


def path_to_string(path):
    return "->".join(path)


if __name__ == '__main__':
    main()
