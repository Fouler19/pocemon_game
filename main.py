from logic import Pokemon, Wizard, Fighter


p1 = Pokemon("Alice")
p2 = Wizard("Bob")
p3 = Fighter("Charlie")


print(p1.info())
print(p1.feed())
print(p2.feed())
print(p3.feed())


print(p1.attack(p2))
print(p3.attack(p1))
