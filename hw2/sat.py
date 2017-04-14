
# sat :: [[String]] -> Bool
def sat(cnf):
    return True

def main():
    # some test cases
    # (a \/ b \/ !c) /\ (b \/ c)
    test([["a","b","!c"], ["b","c"]],                    True)

    # a /\ !a
    test([["a"],["!a"]],                                 False)

    # (a \/ b \/ !c) /\ (a \/ !b \/ c) /\ (!a \/ b \/ c)
    test([["a","b","!c"],["a","!b","c"],["!a","b","c"]], False)

    # (a \/ b) /\ (!a \/ b) /\ (a \/ !b)
    test([["a","b"],["!a","b"],["a","!b"]],              False)

    # (a \/ b) /\ (!a \/ b \/ c) /\ (a \/ !b \/ c)
    test([["a","b"],["!a","b","c"],["a","!b","c"]],      True)
    
    # a \/ b \/ c
    test([["a","b","c"]],                                True)

def test(cnf, answer):
    print("%s %s is %s" %                                   \
       ("correct! " if sat(cnf) == answer else "ERROR!   ", \
        cnf,                                                \
        "satisfiable" if answer else "unsatisfiable"))

if __name__ == "__main__":
    main()
