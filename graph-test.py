#!/usr/bin/env python3

import unittest
from graph import UndirectedGraph


class TestUndirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = UndirectedGraph("graph.csv")

    def test_path_to_self(self):
        shortest_path = self.graph.shortest_path('A', 'A')
        expected_path = ['A']
        expected_cost = 0

        self.assertListEqual(shortest_path['path'], expected_path)
        self.assertEqual(shortest_path['cost'], expected_cost)

    def test_path_symmetry(self):
        shortest_path_1 = self.graph.shortest_path('A', 'B')
        shortest_path_2 = self.graph.shortest_path('B', 'A')
        expected_path_1 = ['A', 'B']
        expected_path_2 = ['B', 'A']
        expected_cost = 5

        self.assertListEqual(shortest_path_1['path'], expected_path_1)
        self.assertListEqual(shortest_path_2['path'], expected_path_2)
        self.assertEqual(shortest_path_1['cost'], expected_cost)
        self.assertEqual(shortest_path_2['cost'], expected_cost)

    def test_no_path(self):
        shortest_path = self.graph.shortest_path('A', 'I')
        expected_cost = float('inf')

        self.assertIsNone(shortest_path['path'])
        self.assertEqual(shortest_path['cost'], expected_cost)

    def test_shortest_paths(self):
        shortest_path_1 = self.graph.shortest_path('C', 'F')
        shortest_path_2 = self.graph.shortest_path('F', 'G')
        shortest_path_3 = self.graph.shortest_path('F', 'C')
        expected_path_1 = ['C', 'G', 'H', 'F']
        expected_path_2 = ['F', 'H', 'G']
        expected_path_3 = ['F', 'H', 'G', 'C']
        expected_cost_1 = 10
        expected_cost_2 = 8
        expected_cost_3 = 10

        self.assertListEqual(shortest_path_1['path'], expected_path_1)
        self.assertListEqual(shortest_path_2['path'], expected_path_2)
        self.assertListEqual(shortest_path_3['path'], expected_path_3)
        self.assertEqual(shortest_path_1['cost'], expected_cost_1)
        self.assertEqual(shortest_path_2['cost'], expected_cost_2)
        self.assertEqual(shortest_path_3['cost'], expected_cost_3)

    def test_load_graph_invalid_cost(self):
        with self.assertRaises(ValueError):
            UndirectedGraph("test/graph-with-invalid-cost.csv")

    def test_load_graph_negative_cost(self):
        with self.assertRaises(ValueError):
            UndirectedGraph("test/graph-with-negative-cost.csv")

    def test_load_graph_invalid_line(self):
        with self.assertRaises(ValueError):
            UndirectedGraph("test/graph-with-invalid-line.csv")

    def test_load_graph_conflicting_lines(self):
        with self.assertRaises(ValueError):
            UndirectedGraph("test/graph-with-conflicting-lines.csv")

    def test_load_graph_duplicate_non_conflicting_lines(self):
        try:
            UndirectedGraph("test/graph-with-duplicate-non-conflicting-lines.csv")
        except ValueError:
            self.fail("Graph file contains duplicate, but non-conflicting edges.")

    def test_load_graph(self):
        expected_nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        expected_edges_A = {'B': 5, 'D': 3, 'E': 4}
        expected_edges_B = {'A': 5, 'C': 4}
        expected_edges_C = {'B': 4, 'G': 2}
        expected_edges_D = {'A': 3, 'G': 6}
        expected_edges_E = {'A': 4, 'F': 6}
        expected_edges_F = {'E': 6, 'H': 5}
        expected_edges_G = {'C': 2, 'D': 6, 'H': 3}
        expected_edges_H = {'F': 5, 'G': 3}
        expected_edges_I = {}

        self.assertCountEqual(self.graph.nodes, expected_nodes)
        self.assertDictEqual(self.graph.edges['A'], expected_edges_A)
        self.assertDictEqual(self.graph.edges['B'], expected_edges_B)
        self.assertDictEqual(self.graph.edges['C'], expected_edges_C)
        self.assertDictEqual(self.graph.edges['D'], expected_edges_D)
        self.assertDictEqual(self.graph.edges['E'], expected_edges_E)
        self.assertDictEqual(self.graph.edges['F'], expected_edges_F)
        self.assertDictEqual(self.graph.edges['G'], expected_edges_G)
        self.assertDictEqual(self.graph.edges['H'], expected_edges_H)
        self.assertDictEqual(self.graph.edges['I'], expected_edges_I)


if __name__ == '__main__':
    unittest.main()
