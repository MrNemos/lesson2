class A:
    def __innit__(self, atr1,atr2):
        self.atr1=atr1
        self.atr2=atr2
        print('Initialisation "A"')

    def __get__(self, instance, owner):
        return {f'{self}:{"atr1":f{self.atr1},"atr2":f{self.atr2}}'}

    def __repr__(self):
        return f'{self} and {self.atr1},{self.atr2}'









a = A()
print(a)