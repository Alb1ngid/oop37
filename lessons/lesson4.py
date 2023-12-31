# инкапсуляция ...
# уровни доступа 3-публиный,защищенный,скрытый

# Java C

# Python

# JS,TS


# наследование полиморфизм

class Bank:
    nameB = 'Бакай'
    money = 1_000_000

    def __init__(self, name, _key, schet):
        self.name = name
        self._key = _key
        self.mon = schet

    def printKEY(self):
        print(self.name, self._key)


bakai = Bank('Бакай', 4862, 0)
bakai.age = 20
bakai.key = 2525
bakai.printKEY()
print(bakai.age, bakai.key)


class Bank2(Bank):
    nameB = 'Оптима'

    def __init__(self, name, _key, schet):
        super().__init__(name, _key, schet)
        self.__schet = schet

    def printKEY(self):
        super().printKEY()
        print(self.__schet)


adil = Bank2('адиль', 4169, 1_000)
adil.__schet = 100000000
adil.key = 1111
adil._key = 1111
adil.printKEY()
adil._Bank2__schet = 100000000
adil.printKEY()
print(dir(Bank2))
print(dir(adil))


class Bank3(Bank2):
    def __init__(self, name, _key, schet, l):
        super().__init__(name, _key, schet)
        self.l = l

    def getKEY(self):
        print(self._key)

    def setKEY(self, key):
        self._key = key


c = Bank3('m', 123, 12343, 'l')
# c.printKEY()
# print(c.l)

c.setKEY(222)
c.getKEY()
# print(Bank3.mro())
