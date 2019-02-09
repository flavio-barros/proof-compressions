from datetime import datetime
from util import constants as const

import csv
import networkx as nx


def get_conclusion_formulas(files):
    formulas = []
    for f in files:
        file_path = "{0}/{1}".format(const.PROOFS_DIR, f)
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

    header = ["file", "conclusion_size", "file_size", "comp_file_size",
              "exec_time"]

    date_now = datetime.now()
    file_path = "{0}/{1}-{2}.csv".format(
        const.LOGS_DIR, algorithm, str(date_now))
    with open(file_path, "wb") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_log)

