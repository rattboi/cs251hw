from __future__ import print_function

######################################
# Expr
#  methods
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Expr:

    def __str__():
        pass

    def rename():
        pass

######################################
# Var <: Expr
#  fields
#    name : String
#  methods
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Var(Expr):

    def __init__(self, n):
        self.name = n

    def __str__(self):
        return self.name

    def rename(self, x, z):
        if self.name == x:
            return Var(z)
        else:
            return Var(self.name)

######################################
# Not <: Expr
#  fields
#    body : Expr
#  methods 
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Not(Expr):

    def __init__(self, b):
        self.body = b

    def __str__(self):
        return "! ({})".format(self.body)

    def rename(self, x, z):
        return Not(self.body.rename(x, z))

######################################
# And <: Expr
#  fields
#    left  : Expr
#    right : Expr
#  methods
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class And(Expr):

    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        return "({}) /\\ ({})".format(self.left, self.right)

    def rename(self, x, z):
        return And(self.left.rename(x, z), self.right.rename(x, z))

######################################
# Or <: Expr
#  fields
#    left  : Expr
#    right : Expr
#  methods 
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Or(Expr):

    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        return "({}) \\/ ({})".format(self.left, self.right)

    def rename(self, x, z):
        return Or(self.left.rename(x, z), self.right.rename(x, z))

######################################
# Arrow <: Expr
#  fields
#    left  : Expr
#    right : Expr
#  methods 
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Arrow(Expr):

    def __init__(self, l, r):
        self.left = l
        self.right = r

    def __str__(self):
        return "({}) -> ({})".format(self.left, self.right)

    def rename(self, x, z):
        return Arrow(self.left.rename(x, z), self.right.rename(x, z))

######################################
# Forall <: Expr
#  fields
#    var  : String
#    body : Expr
#  methods
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Forall(Expr):

    def __init__(self, v, b):
        self.var = v
        self.body = b

    def __str__(self):
        return "A {}. ({})".format(self.var, self.body)

    def rename(self, x, z):
        if self.var == x:
            return Forall(z, self.body.rename(x, z))
        else:
            return Forall(self.var, self.body.rename(x, z))

######################################
# Exists <: Expr
#  fields
#    var : String
#    body : Expr
#  methods
#    __str__ : Expr -> String
#    rename   : Expr -> Expr
######################################

class Exists(Expr):

    def __init__(self, v, b):
        self.var = v
        self.body = b

    def __str__(self):
        return "E {}. ({})".format(self.var, self.body)

    def rename(self, x, z):
        if self.var == x:
            return Exists(z, self.body.rename(x, z))
        else:
            return Exists(self.var, self.body.rename(x, z))

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
    forms = [(form1, ("x", "z")),
             (form2, ("x", "y")),
             (form3, ("y", "z")),
             (form4, ("y", "z")),
             (form5, ("x", "y")),
             (form6, ("y", "q"))]
    for t in enumerate(forms):
        (probNum, (form, (origVar, renameVar))) = t
        print("{}. {} [{} |-> {}] = {}".format(probNum + 1,
                                               form,
                                               origVar,
                                               renameVar,
                                               form.rename(origVar, renameVar)))

if __name__ == '__main__':
    main()
