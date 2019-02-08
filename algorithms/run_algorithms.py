from util import constants as const
from os import listdir
from os.path import isfile, join
from log import log

import time
import random
import itertools


def run_algorithms(algorithms):

    path = const.PROOFS_DIRECTORY + "/"
    files = [f for f in listdir(path) if isfile(join(path, f))]

    formulas = log.get_conclusion_formulas(files)

    for alg in algorithms:
        algorithm_log = []
        algorithm_impl = identify_algorithms(alg)
        for (file_name, formula) in itertools.izip(files, formulas):
            proof_log = [file_name, len(formula)]
            print "run", alg, "in file", file_name, "formula with", \
                len(formula), "characters"
            exec_time = run_algorithm(file, algorithm_impl)
            print "executed in", exec_time, "seconds"
            proof_log.append(exec_time)
            algorithm_log.append(proof_log)
        log.write_log(alg, algorithm_log)


def run_algorithm(file, function):
    start_time = time.time()

    rand_time = random.randint(1, 3)
    time.sleep(rand_time)

    elapsed_time = time.time() - start_time

    return round(elapsed_time, 2)


def run_huffman_coding(file):
    pass


def run_horizontal_compression(file):
    pass


def identify_algorithms(algorithm_constant):
    if algorithm_constant == const.HUFFMAN_CODING:
        return run_huffman_coding
    elif algorithm_constant == const.HORIZONTAL_COMPRESSING:
        return run_horizontal_compression

    return None

