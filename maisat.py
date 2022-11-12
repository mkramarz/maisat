import sys
import time
from formula import *
from dpll import dpll

try:
    file = sys.argv[1]
except IndexError:
    print("Script was run without arguments, defaulting to demo CNF file")
    file = "./problems/easy.cnf"

with open(file) as f:
    lines = f.read()
formula = Formula(lines)

start_time = time.time()
res = dpll(formula)
total_time = time.time() - start_time
status = "SAT" if res else "UNSAT"
print(f"Problem was found to be {status}")
print(f"We finished execution in {format(total_time, '.8f')}s")