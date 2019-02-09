#!/usr/local/bin/python
# coding: utf-8

from heapq import heappush, heappop
from util import constants as const

import bitarray
import os

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

    def __init__(self, file_name):
        self.file_name = file_name
        self.file_path = "{0}/{1}".format(const.PROOFS_DIR, file_name)
        bin_name = "{0}-{1}".format(const.HUFFMAN_CODING,
                                    self.file_name.replace(".dot", ""))
        self.comp_file_path = "{0}/{1}.bin".format(const.C_PROOFS_DIR, bin_name)
        self.characters = []
        self.frequencies = []
        self.codes = {}
        self.queue = []

        self.get_frequencies()
        self.generate_codes()

    def generate_codes(self):

        for i in range(0, len(self.characters)):
            node = HuffmanNode(self.characters[i], self.frequencies[i])
            heappush(self.queue, node)

        root = None

        while len(self.queue) > 1:
            min_node1 = heappop(self.queue)
            min_node2 = heappop(self.queue)

            frequency = min_node1.frequency + min_node2.frequency
            internal_node = HuffmanNode("$", frequency)

            internal_node.leftChild = min_node1
            internal_node.rightChild = min_node2

            root = internal_node

            heappush(self.queue, internal_node)

        self.print_code(root, "")

    def print_code(self, node, code):
        if not node.rightChild and not node.leftChild:
            self.codes[node.character] = code
            return
        else:
            self.print_code(node.leftChild, code + "0")
            self.print_code(node.rightChild, code + "1")

    def get_frequencies(self):
        data = dict()

        print self.file_path
        with open(self.file_path) as dot_file:
            text = dot_file.read()
            for c in text:
                if c in data:
                    data[c] += 1
                else:
                    data[c] = 1

        for key, value in sorted(data.iteritems(), key=lambda (k, v): (v, k)):
            self.characters.append(key)
            self.frequencies.append(value)

    def compress(self):
        bits = ""
        with open(self.file_path) as dot_file:
            text = dot_file.read()
            for c in text:
                bits += self.codes[c]

        bits = bitarray.bitarray(bits)
        with open(self.comp_file_path, "wb") as f:
            bits.tofile(f)

        size = os.stat(self.file_path).st_size
        comp_size = os.stat(self.comp_file_path).st_size

        return size, comp_size
