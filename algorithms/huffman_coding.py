#!/usr/local/bin/python
# coding: utf-8

from heapq import heappush, heappop

"""
code adapted from https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/
"""


class HuffmanNode(object):

    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.leftChild = None
        self.rightChild = None

    def __le__(self, other):
        return self.frequency <= other.frequency

    def __repr__(self):
        return "(" + str(self.character) + " - " + str(self.frequency) + ")"


class Huffman(object):

    def __init__(self, text):
        self.characters, self.frequencies = Huffman.sort_characters(text)
        self.root = None
        self.codes = {}
        self.queue = []

    def generate_codes(self):

        for i in range(0, len(self.characters)):
            node = HuffmanNode(self.characters[i], self.frequencies[i])
            heappush(self.queue, node)

        while len(self.queue) > 1:
            min_node1 = heappop(self.queue)
            min_node2 = heappop(self.queue)

            frequency = min_node1.frequency + min_node2.frequency
            internal_node = HuffmanNode("$", frequency)

            internal_node.leftChild = min_node1
            internal_node.rightChild = min_node2

            self.root = internal_node

            heappush(self.queue, internal_node)

        self.print_code(self.root, "")

    def print_code(self, node, code):
        if not node.rightChild and not node.leftChild:
            self.codes[node.character] = code
            return
        else:
            self.print_code(node.leftChild, code + "0")
            self.print_code(node.rightChild, code + "1")

    @staticmethod
    def sort_characters(text):
        data = dict()
        characters = list()
        frequencies = list()

        for c in text:
            if c in data:
                data[c] += 1
            else:
                data[c] = 1

        for key, value in sorted(data.iteritems(), key=lambda (k, v): (v, k)):
            characters.append(key)
            frequencies.append(value)

        return characters, frequencies
