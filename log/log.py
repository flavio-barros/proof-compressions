from datetime import datetime
from util import constants as const

import csv
import networkx as nx


def get_conclusion_formulas(files):
    formulas = []
    for f in files:
        file_path = "{0}/{1}".format(const.PROOFS_DIRECTORY, f)
        agraph = nx.nx_agraph.read_dot(file_path)
        graph = nx.DiGraph(agraph)

        conclusions = []

        for node in list(graph.nodes):
            if graph.out_degree(node) == 0:
                conclusions.append(node)

        conclusion, = conclusions
        formula = graph.nodes[conclusion]["label"]
        formulas.append(formula.replace(" ", ""))
    return formulas


def write_log(algorithm, data_log):

    date_now = datetime.now()
    file_path = "{0}/{1}-{2}.csv".format(
        const.LOGS_DIRECTORY, algorithm, str(date_now))
    with open(file_path, "wb") as f:
        writer = csv.writer(f)
        writer.writerows(data_log)

