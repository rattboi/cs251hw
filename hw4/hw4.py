#!/usr/bin/env python3.6

from typing import List, Tuple

class Expr:
    """
    Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __str__(self) -> str:
        pass

    def rename(self, x: str, z: str) -> 'Expr':
        raise NotImplementedError


class Var(Expr):
    """
    Var <: Expr
     fields
       name : String
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, n) -> None:
        self.name = n

    def __str__(self) -> str:
        return self.name

    def rename(self, x: str, z: str) -> Expr:
        return Var(z if self.name == x else self.name)


class Not(Expr):
    """
    Not <: Expr
     fields
       body : Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, b: Expr) -> None:
        self.body = b

    def __str__(self) -> str:
        return f'¬({self.body})'

    def rename(self, x: str, z: str) -> Expr:
        return Not(self.body.rename(x, z))


class And(Expr):
    """
    And <: Expr
     fields
       left  : Expr
       right : Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, l: Expr, r: Expr) -> None:
        self.left = l
        self.right = r

    def __str__(self) -> str:
        return f'({self.left}) ∧ ({self.right})'

    def rename(self, x: str, z: str) -> Expr:
        return And(self.left.rename(x, z), self.right.rename(x, z))


class Or(Expr):
    """
    Or <: Expr
     fields
       left  : Expr
       right : Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, l: Expr, r: Expr) -> None:
        self.left = l
        self.right = r

    def __str__(self) -> str:
        return f'({self.left}) ∨ ({self.right})'

    def rename(self, x: str, z: str) -> Expr:
        return Or(self.left.rename(x, z), self.right.rename(x, z))


class Arrow(Expr):
    """
    Arrow <: Expr
     fields
       left  : Expr
       right : Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, l: Expr, r: Expr) -> None:
        self.left = l
        self.right = r

    def __str__(self) -> str:
        return f'({self.left}) → ({self.right})'

    def rename(self, x: str, z: str) -> Expr:
        return Arrow(self.left.rename(x, z), self.right.rename(x, z))


class Forall(Expr):
    """
    Forall <: Expr
     fields
       var  : String
       body : Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, v: str, b: Expr) -> None:
        self.var = v
        self.body = b

    def __str__(self) -> str:
        return f'∀{self.var}.({self.body})'

    def rename(self, x: str, z: str) -> Expr:
        return Forall(z if self.var == x else self.var, self.body.rename(x, z))


class Exists(Expr):
    """
    Exists <: Expr
     fields
       var : String
       body : Expr
     methods
       __str__  : Expr -> String
       rename   : Expr -> Expr
    """

    def __init__(self, v: str, b: Expr) -> None:
        self.var = v
        self.body = b

    def __str__(self) -> str:
        return f'∃{self.var}.({self.body})'

    def rename(self, x: str, z: str) -> Expr:
        return Exists(z if self.var == x else self.var, self.body.rename(x, z))


def print_forms(forms: List[Tuple[Expr, Tuple[str, str]]]) -> None:
    for (probNum, (form, (origVar, renameVar))) in enumerate(forms):
        print(f'{probNum + 1}. {form} [{origVar} ↦ {renameVar}] = {form.rename(origVar, renameVar)}')


def main() -> None:
    """
    Main and tests
    """

    form1 = And(Var("x"), Var("x"))
    form2 = And(Var("x"), Forall("x", Var("x")))
    form3 = And(Exists("y", Var("y")), Forall("x", Var("x")))
    form4 = Forall("x", Arrow(Var("x"), And(Var("x"), Var("y"))))
    form5 = Not(And(Forall("x", Var("x")), Var("x")))
    form6 = Not(Forall("x", Var("y")))
    forms = [(form1, ("x", "z")),
             (form2, ("x", "y")),
             (form3, ("y", "z")),
             (form4, ("y", "z")),
             (form5, ("x", "y")),
             (form6, ("y", "q"))]
    print_forms(forms)


if __name__ == '__main__':
    main()
