# Takes lists of items and enchantments and produces combinations
from tkinter import *
from tkinter.ttk import *
import enchantImporter
import weaponImporter

# Create Window
window = Tk()

weapons = weaponImporter.main()
enchantments = enchantImporter.main()


def setWeapon(chosen_weapon):
    currentWeapon = chosen_weapon


def setEnchantment(chosen_enchantment):
    currentEnchantment = chosen_enchantment


for weapon in weapons:
    button = Button(text=weapon, command=setWeapon(weapon))
    button.pack()
    print(weapon)

window.mainloop()

print('Please choose a melee weapon: ')
weaponName = input()

for enchant in enchantments:
    print(enchant)

print('Please choose an enchantment: ')
enchantmentName = input()

# List for possible weapon matches

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
