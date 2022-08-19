# Enchantment Class
# Combined with items to modify attributes
# Includes spell name, effects, base item, cost, prefix, suffix, notes

class enchantment:

    def __init__(self, name, effect, base_item, cost, prefix, suffix, notes1 = None):
        self.name = name
        self.effect = effect
        self.base_item = base_item
        self.cost = cost
        self.prefix = prefix
        self.suffix = suffix

    def __str__(self):
        return self.name
