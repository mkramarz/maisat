from copy import deepcopy
import random
from formula import *

def dpll(formula: Formula):
    bcp(formula)
    if not formula.clauses: #All clauses SAT -> formula is SAT
        print(f'Assignment {formula.assignments} is satisfiable!')
        return True
    if tuple() in formula.clauses: #UNSAT Clause -> this branch is UNSAT
        return False
    try:
        choice = random.choice([id for id, val in enumerate(formula.assignments) if id != 0 and val == 0]) #Pick unassigned var
    except IndexError:
        return False #This shouldn't happen.

    formula_if_true = deepcopy(formula)
    formula_if_true.assignments[choice] = 1
    formula_if_true.update_clauses()

    formula_if_false = deepcopy(formula)
    formula_if_false.assignments[choice] = -1
    formula_if_false.update_clauses()
    
    return dpll(formula_if_true) or dpll(formula_if_false)

#Mutates formula until no more unit propagation is possible
def bcp(formula: Formula):
    continue_bcp = True
    while continue_bcp:
        continue_bcp = False
        for clause in formula.clauses:
            if len(clause) == 1:
                var = clause[0]
                id = abs(var)
                val = 1 if var >= 0 else -1
                formula.assignments[id] = val
                formula.update_clauses()
                continue_bcp = True