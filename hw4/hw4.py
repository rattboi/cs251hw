from __future__ import print_function

######################################
# Expr
#  methods
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Expr:

    def toString():
        pass

    def rename():
        pass

######################################
# Var <: Expr
#  fields 
#    name : String
#  methods 
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Var(Expr):

    def __init__(self, n):
        self.name = n

    def toString(self):
        return self.name

    def rename(self, x, z):
        if self.name == x:
            self.name = z
        return self

######################################
# Not <: Expr
#  fields
#    body : Expr
#  methods 
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Not(Expr):

    def __init__(self, b):
        self.body = b

    def toString(self):
        return "! (" + self.body.toString() + ")"

    def rename(self, x, z):
        self.body.rename(x, z)
        return self

######################################
# And <: Expr
#  fields
#    left  : Expr
#    right : Expr
#  methods
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class And(Expr):

    def __init__(self, l, r):
        self.left = l
        self.right = r

    def toString(self):
        return "(" + self.left.toString() + ") /\\ (" + self.right.toString() + ")"

    def rename(self, x, z):
        self.left.rename(x, z)
        self.right.rename(x, z)
        return self

######################################
# Or <: Expr
#  fields
#    left  : Expr
#    right : Expr
#  methods 
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Or(Expr):

    def __init__(self, l, r):
        self.left = l
        self.right = r

    def toString(self):
        return "(" + self.left.toString() + ") \\/ (" + self.right.toString() + ")"

    def rename(self, x, z):
        self.left.rename(x, z)
        self.right.rename(x, z)
        return self

######################################
# Arrow <: Expr
#  fields
#    left  : Expr
#    right : Expr
#  methods 
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Arrow(Expr):

    def __init__(self, l, r):
        self.left = l
        self.right = r

    def toString(self):
        return "(" + self.left.toString() + ") -> (" + self.right.toString() + ")"

    def rename(self, x, z):
        self.left.rename(x, z)
        self.right.rename(x, z)
        return self

######################################
# Forall <: Expr
#  fields
#    var  : String
#    body : Expr
#  methods
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Forall(Expr):

    def __init__(self, v, b):
        self.var = v
        self.body = b

    def toString(self):
        return "A " + self.var + ". (" + self.body.toString() + ")"

    def rename(self, x, z):
        if self.var == x:
            self.var = z
        self.body.rename(x, z)
        return self

######################################
# Exists <: Expr
#  fields
#    var : String
#    body : Expr
#  methods
#    toString : Expr -> String
#    rename   : Expr -> Expr
######################################

class Exists(Expr):

    def __init__(self, v, b):
        self.var = v
        self.body = b

    def toString(self):
        return "E " + self.var + ". (" + self.body.toString() + ")"

    def rename(self, x, z):
        if self.var == x:
            self.var = z
        self.body.rename(x, z)
        return self

######################################
# Main and tests
######################################

def main():
    form1 = And(Var("x"), Var("x"))
    form2 = And(Var("x"), Forall("x", Var("x")))
    form3 = And(Exists("y", Var("y")), Forall("x", Var("x")))
    form4 = Forall("x", Arrow(Var("x"), And(Var("x"), Var("y"))))
    form5 = Not(And(Forall("x", Var("x")), Var("x")))
    form6 = Not(Forall("x", Var("y")))
    print(form1.toString() + "[x |-> z] = " + form1.rename("x", "z").toString() + "\n")
    print(form2.toString() + "[x |-> y] = " + form2.rename("x", "y").toString() + "\n")
    print(form3.toString() + "[y |-> z] = " + form3.rename("y", "z").toString() + "\n")
    print(form4.toString() + "[y |-> z] = " + form4.rename("y", "z").toString() + "\n")
    print(form5.toString() + "[x |-> y] = " + form5.rename("x", "y").toString() + "\n")
    print(form6.toString() + "[y |-> q] = " + form6.rename("y", "q").toString() + "\n")

if __name__ == '__main__':
    main()
