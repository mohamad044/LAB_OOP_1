from panda_class import Panda

panda1 = Panda("a", 5, 100, "leaves")
panda2 = Panda("b", 3, 80, "fruits")
panda3 = Panda("c", 7, 120, "fruits")
panda4 = Panda("d", 4, 90, "leaves")

print(panda1.name)
print(panda2.name)


for panda in [panda1, panda2, panda3, panda4]:
    panda.wieght()
    panda.eat()

