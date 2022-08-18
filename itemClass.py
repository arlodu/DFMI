# Item class, baseline for weapons and armor,
# includes base cost, weight, and name

class item:

    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
