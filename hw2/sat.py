# sat :: [[String]] -> Bool
def sat(cnf):
    cases = generate_cases()
    results = []
    for case in cases:
        results.append(all([check_clause(clause, case) for clause in cnf]))
    return any(results)


def generate_cases():
    return [(a, b, c) for a in [False, True] for b in [False, True] for c in [False, True]]


def check_clause(clause, case):
    return any([check_var(var, case) for var in clause])


def check_var(var, case):
    (a, b, c) = case
    if var == "a" and a is True:
        return True
    if var == "!a" and a is False:
        return True
    if var == "b" and b is True:
        return True
    if var == "!b" and b is False:
        return True
    if var == "c" and c is True:
        return True
    if var == "!c" and c is False:
        return True
    if var == "T":
        return True
    return False


def main():
    # some test cases
    # (a \/ b \/ !c) /\ (b \/ c)
    test([["a", "b", "!c"], ["b", "c"]],                         True)

    # a /\ !a
    test([["a"], ["!a"]],                                        False)

    # (a \/ b \/ !c) /\ (a \/ !b \/ c) /\ (!a \/ b \/ c)
    test([["a", "b", "!c"], ["a", "!b", "c"], ["!a", "b", "c"]], True)

    # (a \/ b) /\ (!a \/ b) /\ (a \/ !b)
    test([["a", "b"], ["!a", "b"], ["a", "!b"]],                 True)

    # (a \/ b) /\ (!a \/ b \/ c) /\ (a \/ !b \/ c)
    test([["a", "b"], ["!a", "b", "c"], ["a", "!b", "c"]],       True)

    # a \/ b \/ c
    test([["a", "b", "c"]],                                      True)

def test(cnf, answer):
    print("%s %s is %s" %                                        \
            ("correct! " if sat(cnf) == answer else "ERROR!   ", \
            cnf,                                                 \
            "satisfiable" if answer else "unsatisfiable"))

if __name__ == "__main__":
    main()
