import random
class TQuadrangle:
    def __init__(self, *args):
        if len(args) == 0:
            self.a = random.random() * 10
            self.b = random.random() * 10
        elif len(args) == 1:
            self.a = int(args[0])
            self.b = random.random() * 10
        elif len(args) == 2:
            self.a = int(args[0])
            self.b = int(args[1])

    def s(self):
        return self.a * self.b

    def p(self):
        return (self.a + self.b) * 2


class Tpryamok(TQuadrangle):
    def __init__(self,*args):
        super().__init__(*args)
        if self.a == self.b:
            print('це не прямокутник')


class Tsc(Tpryamok):
    def __init__(self,*args):
        super().__init__(*args)
        self.b = self.a


class Tparalel(Tsc):
    def __init__(self,*args):
        super().__init__(*args)


n = int(input('введіть значення n'))
elems = []
for i in range(n):
    k = int(random.random() * 4)
    if k == 1:
        elems.append(TQuadrangle())
    elif k == 2:
        elems.append(Tpryamok())
    else:
        elems.append(Tsc())

sq = [el.p() for el in elems]


print(sum(sq))