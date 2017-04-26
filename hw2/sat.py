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
    (a_case, b_case, c_case) = case
    var_lookup = {"a": True, "!a": False,
                  "b": True, "!b": False,
                  "c": True, "!c": False,
                  "T": True}

    case_lookup = {"a": a_case, "!a": a_case,
                   "b": b_case, "!b": b_case,
                   "c": c_case, "!c": c_case,
                   "T": True}

    return (var_lookup[var] == case_lookup[var])


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


    test([["a", "b", "c"], ["a", "b", "!c"], ["a", "!b", "c"], ["a", "!b", "!c"], ["!a", "b", "c"], ["!a", "b", "!c"], ["!a", "!b", "c"], ["!a", "!b", "!c"], ["a", "b", "c"], ["a", "b", "!c"], ["a", "!b", "c"], ["a", "!b", "!c"], ["!a", "b", "c"], ["!a", "b", "!c"], ["!a", "!b", "c"], ["!a", "!b", "!c"]], False)


def test(cnf, answer):
    print("%s %s is %s" %                                        \
            ("correct! " if sat(cnf) == answer else "ERROR!   ", \
            cnf,                                                 \
            "satisfiable" if answer else "unsatisfiable"))

if __name__ == "__main__":
    main()
