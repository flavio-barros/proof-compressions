#!/usr/local/bin/python
# coding: utf-8

# from algorithms import run_algorithms as alg
# from util.constants import HORIZONTAL_COMPRESSING, HUFFMAN_CODING
from generator import formula

def main():
    # algorithms = [HORIZONTAL_COMPRESSING, HUFFMAN_CODING]
    # alg.run_algorithms(algorithms)

    formula.generate_fibonacci_formulas(100)


if __name__ == '__main__':
    main()
