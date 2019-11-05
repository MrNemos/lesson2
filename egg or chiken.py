
class Egg():
    pass
class Chiken(Egg):
    def __init__(self,name,parent=1,parentlist = list([])):
        self.name = name
        self.parent = parent
        print(parentlist)
        self.parentlist = parentlist + [parent]
        print(self.parentlist)

    def child(self,name):
        n = self.parent
        parentlist = self.parentlist
        return Egg(name,n,parentlist)
    def __str__(self):
        return f'{self.name} {self.parent} {self.parentlist}'

class Egg(Chiken):
    def __init__(self,name,parent,parentlist):
        print(parentlist)
        super.__init__(name,parent,parentlist)

    def child(self):
        name = self.name
        parent = self.parent
        parentlist = self.parentlist
        return Chiken(name,parent,parentlist)

chiken1 = Chiken("Cipa",'Cura')
print(chiken1)
egg2 = chiken1.child('Cipa2')
chiken2 = egg2.child()

