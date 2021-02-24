#!/usr/bin/env python3

from graph import UndirectedGraph


def main():
    graph_filename = input("Graph filename: ")
    start_node = input("Start node: ")
    end_node = input("End node: ")

    graph = UndirectedGraph(graph_filename)
    shortest_path = graph.shortest_path(start_node, end_node)
    if shortest_path['path'] is None:
        print(f"There is no path connecting {start_node} to {end_node}.")
    else:
        print(f"Path from {start_node} to {end_node} is {path_to_string(shortest_path['path'])},",
              f"and have cost {shortest_path['cost']}.")


def path_to_string(path):
    return "->".join(path)


if __name__ == '__main__':
    main()
