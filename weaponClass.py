# weapon class, extends item class

from itemClass import item

item1 = item("sword", 4, 20)

#print(item1.name, item1.weight)

class weapon(item):

    def __init__(self, name, weight, cost, \
    skill1, damage1, reach1, parry1, ST1, notes, \
    skill2 = None, damage2 = None, reach2 = None, parry2 = None, ST2 = None,\
    skill3 = None, damage3 = None, reach3 = None, parry3 = None, ST3 = None):
        super().__init__(name, weight, cost)
        self.skill1 = skill1
        self.damage1 = damage1
        self.reach1 = reach1
        self.parry1 = parry1
        self.ST1 = ST1
        self.notes = notes

weapon1 = weapon("smallsword", 4, 20, "smallsword DX-3", "thr imp", "C,1", "0U", 5, ())
print(weapon1.reach1)
