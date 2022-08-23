#Takes lists of items and enchantments and produces combinations

import enchantImporter
import weaponImporter



weapons = weaponImporter.main()
enchantments = enchantImporter.main()

for weapon in weapons:
    print(weapon)

print('Please choose a melee weapon: ')
weaponName = input()

for enchant in enchantments:
    print(enchant)

print('Please choose an enchantment: ')
enchantmentName = input()

#List for possible weapon matches

for weapon in weapons:
    if weaponName.lower() == weapon.lower().lstrip():
        weaponName = weapon

for enchant in enchantments:
    if enchantmentName.lower() == enchant.lower().lstrip():
        enchantName = enchant

enchantCost = enchantments[enchantName].cost
enchantCost = enchantCost.replace('$', '')
enchantCost = int(enchantCost.replace(',', ''))

weaponCost = weapons[weaponName].cost
weaponCost = weaponCost.replace(',', '')
weaponCost = int(weaponCost.replace('$', ''))

totalCost = weaponCost + enchantCost

print(totalCost)
