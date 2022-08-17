# import items from file into dictionary of items by name

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
            refList.append(lineList.copy())
            lineList.clear()
            lineList.append(line.rstrip())
    return refList

#Returns a tuple of the specific weapon's table (a list of lists)
#and the name of the skill as a string for those entries
def weaponTableBuilder(newSource):
    #tracker for position in table
    n = 0
    while n <= len(newSource):
        #Check for skill name and step forward if so
        if 'DX' in newSource[n]:
            skillName = newSource[n]
            n = n+1
            continue
        else:
            wepTabl = newSource[n].copy()
            print(wepTabl)
                if 'or' in newSource[n][0]:
                    print(newSource[n][0])
                    n = n+1
                    if n < len(newSource) and 'or' in newSource[n][0]:
                        print(newSource[n][0])
                        n = n+1
                elif 'two hands' in newSource[n][0]:
                    print(newSource[n][0])
                    n = n+1
                else:
                    print('one line only')


#Returns a weapon object built from recieved tuple from weaponTableBuilder
#def weaponBuilder(skill, table):


weaponDict = {}

file = open("itemList.txt", encoding='utf-8')
source = file.readlines()

weapon1 = weapon("smallsword", 4, 20, "smallsword DX-3", "thr imp", "C,1", "0U", 5, ())

weaponDict[weapon1.name] = weapon1

print(weapon1.name, weapon1.parry1, weapon1.damage1)


#Take the list and construct a list of lists table
#resembling the original table
newSource = refineSource(source)

for line in newSource:
    print(line)

#
weaponTableBuilder(newSource)




#print(newSource[1][4])




# Set last 'added' variable, add two hands condition, or condition, create instantiation function that can do the thing?
