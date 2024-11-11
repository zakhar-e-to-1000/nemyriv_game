from random import randint

class Plashka:
    def __init__(self, name):
        self.name = name
        self.__zirocka = randint(1,2)==1
    def zirochka(self):
        return self.__zirocka


class Alcoholic:
    def __init__(self, name) -> None:
        print("Жив собі", name)
        self.__name = name
        self.__count = 0
        self.__alive = True

    def alive(self):
        return self.__alive

    def zirochka(self):
        if not self.__alive:
            print(self.__name+" вже здох")
            return
        self.__count += 1
        print("Скільки зірочок:", self.__count)
        if self.__count==5:
            self.__alive = False
            self.__name += ' ✝2024'
            print("Здох "+self.__name)
    def vzaty_plashku(self, plashka):
        print(self.__name+" взяв "+plashka.name)
        print(self.__name+", збери 5 зірочок, і тобі кришечка")
        if plashka.zirochka():
            self.zirochka()
        else:
            print("Скільки зірочок: ", self.__count)

print()
ivan = Alcoholic("Іван")
while ivan.alive():
    pl = Plashka("Немирів")
    ivan.vzaty_plashku(pl)

    