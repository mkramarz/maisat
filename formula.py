class Formula:
    def __init__(self, formula: str) -> None:
        lines = formula.split('\n')
        desc = lines[0].split(' ')
        numvars = int(desc[2])
        self.clauses = set()
        self.assignments = [0 for _ in range(0, numvars+1)]
        for line in lines[1:]:
            vars = [line for line in line.split(' ') if line]
            if vars:
                if vars[-1] == '0':
                    clause = tuple([int(i) for i in vars[:-1]])
                else:
                    clause = tuple([int(i) for i in vars])
                self.clauses.add(clause)

    def update_clauses(self):
        # print(f'Clauses: {self.clauses}\nAssignments: {self.assignments}')
        new_clauses = set()

        for clause in self.clauses:
            new_clause = []
            drop_clause = False

            for var in clause:
                id = abs(var) #The variable's id
                val = 1 if var >= 0 else -1 #If the variable is negated or not in the clause
                if self.assignments[id] == 0: #If the variable has no assignment, it stays
                    new_clause.append(var)
                elif val == self.assignments[id]: #If the variable has a satisfying assignment, drop clause
                    drop_clause = True
                    break
                else: #If the variable has an unsatisfying assignment, drop var
                    continue
            
            if not drop_clause:
                # print(f'Clause "{clause}" becomes "{new_clause}".')
                new_clauses.add(tuple(new_clause))
            else:
                # print(f'Clause "{clause}" was dropped.')
                pass
        
        self.clauses = new_clauses