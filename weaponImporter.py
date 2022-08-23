# import weapons from file into dictionary of weapons keyed by name

from weaponClass import weapon


#Returns a list Skill catagories and lists of lines from the imported file
#That mimics the original table's format
# Example of returned table:
# SPEAR (DX‑5, Polearm‑4, or Staff‑2)
# [' Heavy Spear', 'thr+4 imp', '2, 3*', '0U', '$90', '6', '11†']
# ['  or', 'thr+3 cut', '3', '0U', '–', '–', '11†']
def refineSource(sourceList):
    #v tracks individual line lengths
    v=0
    #refined list that will be returned
    refList = []
    #list for individual lines of the original table
    lineList = []
    #loop through the lines in the source file
    for index, line in enumerate(sourceList):
        #if it's a skill title line, append it to refined list
        if 'DX' in line:
            #check if we have an ongoing line of text
            #if so, append that line before the skill title
            if v > 0:
                lineList.append(" ")
                refList.append(lineList.copy())
                lineList.clear()
                v=0
            refList.append(line.rstrip())
            continue
        #if we're at a new line or building one continue to do so
        elif v <= 6:
            lineList.append(line.rstrip())
            v = v+1
            continue
        #If this line has a note, add it and append line to refined list
        elif '[' in line:
            lineList.append(line.rstrip())
            refList.append(lineList.copy())
            lineList.clear()
            v=0
        #If we're done building and no note, append line to refined list
        #Begin building the next line with the current word
        else:
            v=1
            lineList.append(" ")
            refList.append(lineList.copy())
            lineList.clear()
            lineList.append(line.rstrip())
    return refList

#Returns a tuple of the specific weapon's table (a list of lists)
#and the name of the skill as a string for those entries
def weaponTableBuilder(newSource):
    weaponDict = {}

    #tracker for position in table
    n = 0
    wepTabl=[]
    while n < len(newSource):
        #Check for skill name and step forward if so
        if 'DX' in newSource[n]:
            skillName = newSource[n]
            n = n+1
            continue
        else:
            wepTabl.append(newSource[n].copy())
            n = n+1
            if n < len(newSource):
                if 'or' in newSource[n][0]:
                    wepTabl.append(newSource[n].copy())
                    n = n+1
                    if n < len(newSource) and 'or' in newSource[n][0]:
                        wepTabl.append(newSource[n].copy())
                        n = n+1
                elif 'two hands' in newSource[n][0]:
                    wepTabl.append(newSource[n].copy())
                    n = n+1
        wepTup = (wepTabl, skillName)
        wepObj = weaponBuilder(wepTup)
        weaponDict[wepObj.name] = wepObj
        wepTabl.clear()
    return weaponDict


        #send wepTabl to weapon builder function
#Returns a weapon object built from recieved tuple from weaponTableBuilder
def weaponBuilder(wepTup):
    rows = len(wepTup[0])

    match rows:
        case 1:
            # name, weight, cost, \
            # skill1, damage1, reach1, parry1, ST1, notes1, \
            tempWeapon = weapon(wepTup[0][0][0], wepTup[0][0][5], wepTup[0][0][4], \
            wepTup[1], wepTup[0][0][1], wepTup[0][0][2], wepTup[0][0][3], wepTup[0][0][6], wepTup[0][0][7])
        case 2:
            tempWeapon = weapon(wepTup[0][0][0], wepTup[0][0][5], wepTup[0][0][4], \
            wepTup[1], wepTup[0][0][1], wepTup[0][0][2], wepTup[0][0][3], wepTup[0][0][6], wepTup[0][0][7], \
            wepTup[1], wepTup[0][1][1], wepTup[0][1][2], wepTup[0][1][3], wepTup[0][1][6], wepTup[0][1][7])
        case 3:
            tempWeapon = weapon(wepTup[0][0][0], wepTup[0][0][5], wepTup[0][0][4], \
            wepTup[1], wepTup[0][0][1], wepTup[0][0][2], wepTup[0][0][3], wepTup[0][0][6], wepTup[0][0][7], \
            wepTup[1], wepTup[0][1][1], wepTup[0][1][2], wepTup[0][1][3], wepTup[0][1][6], wepTup[0][1][7], \
            wepTup[1], wepTup[0][2][1], wepTup[0][2][2], wepTup[0][2][3], wepTup[0][2][6], wepTup[0][2][7])
        case _:
            print('no length?', wepTup)
    return tempWeapon

def main():



    file = open("itemList.txt", encoding='utf-8')
    source = file.readlines()

    #Take the list and construct a list of lists table
    #resembling the original table
    newSource = refineSource(source)

    weaponDict = weaponTableBuilder(newSource)

    return weaponDict
