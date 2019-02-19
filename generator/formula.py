# coding=utf-8

import string
import random
from util import constants as cont


def generate_general_formulas(qty, length, distinct_formulas):
    """
    Retorna 'qty' fórmulas genéricas de tamanho 'length' com 'distinct_formulas'
    átomos distintos
    """

    formulas = []

    # Selecionar átomos da fórmula
    atoms = list(string.uppercase)
    atoms = atoms[0:distinct_formulas]

    formulas = []

    # Gerar fórmulas
    while qty > 0:
        length_aux = length
        formula = [random.choice(atoms) for i in range(0, length)]
        while length_aux > 1:
            index_imp = random.choice(range(0, len(formula)-1))
            antecedent, consequent = formula[index_imp:index_imp+2]

            if len(formula) > 2:
                if len(consequent) > 2:
                    new_imp = "({} imp {})".format(antecedent, consequent)
                else:
                    new_imp = "({} imp ({}))".format(antecedent, consequent)
            else:
                if len(consequent) > 2:
                    new_imp = "{} imp {}".format(antecedent, consequent)
                else:
                    new_imp = "{} imp ({})".format(antecedent, consequent)

            formula[index_imp] = new_imp
            del formula[index_imp + 1]
            length_aux -= 1
        formulas.append(formula)
        qty -= 1

    print formulas


def generate_tautologies(recursions=1):

    model_formula = "".format()


def generate_fibonacci_formulas(num_atoms=3):

    if num_atoms < 3:
        num_atoms = 3

    atoms = ["A"+str(n) for n in range(1, num_atoms+1)]

    print atoms

    last_formula = "({0} imp ({1}))".format(atoms[0], atoms[num_atoms-1])

    formula = "(({0} imp ({1})) imp (({0} imp ({1} imp ({2})))".format(atoms[0],
                                                                       atoms[1],
                                                                       atoms[2])

    miss_formulas = num_atoms - 3

    with open(cont.FIB_FILE, "w") as fib_file:
        write_fibonacci_formula(formula, atoms, 3, fib_file)
        for i in range(0, miss_formulas):
            index_atom = i + 3
            new = " imp (({} imp ({} imp ({})))".format(atoms[index_atom-2],
                                                        atoms[index_atom-1],
                                                        atoms[index_atom])
            formula += new

            write_fibonacci_formula(formula, atoms, index_atom+1, fib_file)


def write_fibonacci_formula(formula, atoms, num_atom, fib_file):
    last_formula = "({0} imp ({1}))".format(atoms[0], atoms[num_atom-1])
    formula += " imp "+last_formula
    for i in range(0, num_atom-1):
        formula += ")"
    fib_file.write(formula + "\n")
    print formula

