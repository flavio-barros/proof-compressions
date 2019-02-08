#!/usr/local/bin/python
# coding: utf-8

from algorithms import run_algorithms as alg
from util.constants import HORIZONTAL_COMPRESSING, HUFFMAN_CODING


def main():
    algorithms = [HORIZONTAL_COMPRESSING, HUFFMAN_CODING]
    alg.run_algorithms(algorithms)


if __name__ == '__main__':
    main()
