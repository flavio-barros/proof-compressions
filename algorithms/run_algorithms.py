from util import constants as const
from log import log
from algorithms.huffman_coding import Huffman

import time
import itertools
import os

from compressing.horizontal_compression import HorizontalCompression


def run_algorithms(algorithms):
    path = const.PROOFS_DIR + "/"
    files = \
        [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    formulas = log.get_conclusion_formulas(files)

    for alg in algorithms:
        algorithm_log = []
        algorithm_impl = identify_algorithms(alg)
        for (file_name, formula) in itertools.izip(files, formulas):
            print "run", alg, "in file", file_name, "formula with", \
                len(formula), "characters"

            proof_log = [file_name, len(formula)]

            algorithm_data = run_algorithm(file_name, algorithm_impl)
            exec_time, size, comp_size = algorithm_data

            proof_log.append(size)
            proof_log.append(comp_size)
            proof_log.append(exec_time)

            algorithm_log.append(proof_log)

            print "executed in", exec_time, "seconds"
        log.write_log(alg, algorithm_log)


def run_algorithm(file_name, algorithm_impl):
    start_time = time.time()

    size, comp_size = algorithm_impl(file_name)

    elapsed_time = time.time() - start_time

    return round(elapsed_time, 3), size, comp_size


def run_huffman_coding(file_name):
    huffman = Huffman(file_name)
    size, comp_size = huffman.compress()
    return size, comp_size


def run_horizontal_compression(file_name):
    h_compression = HorizontalCompression(file_name)
    return None, None


def identify_algorithms(algorithm_constant):
    if algorithm_constant == const.HUFFMAN_CODING:
        return run_huffman_coding
    elif algorithm_constant == const.HORIZONTAL_COMPRESSING:
        return run_horizontal_compression

    return None
