# import enchantments from file into dictionary of enchantments keyed by name

from enchantClass import enchantment



# Returns a lists of lines from the imported file
# That mimics the original table's format
# Example of returned table:


def refineSource(sourceList):
    #v tracks individual line lengths
    v=0
    #refined list that will be returned
    refList = []
    #list for individual lines of the original table
    lineList = []
    #loop through the lines in the source file
    for index, line in enumerate(sourceList):
        #if we're at a new line or building one continue to do so
        if v <= 5:
            lineList.append(line.rstrip())
            v = v+1
            continue
        #If this line has a note, add it and append line to refined list
        elif '[' in line:
            lineList.append(line.rstrip())
            refList.append(lineList.copy())
            lineList.clear()
            v=0
            continue
        #If we're done building and no note, append line to refined list
        #Begin building the next line with the current word
        else:
            v=1
            lineList.append(" ")
            refList.append(lineList.copy())
            lineList.clear()
            lineList.append(line.rstrip())
    return refList

def enchantTableBuilder(newSource):
    #tracker for position in table
    enchantDict = {}
    n = 0
    encTabl=[]
    while n < len(newSource):
        encObj = enchantBuilder(newSource[n].copy())
        n = n+1
        enchantDict[encObj.name+'_'+encObj.base_item] = encObj
        encTabl.clear()
    return enchantDict

def enchantBuilder(encTabl):
    tempEnc = enchantment(encTabl[0],encTabl[1],encTabl[2],encTabl[3], \
                        encTabl[4], encTabl[5], encTabl[6])
    return tempEnc

def main():
    file = open("enchantList.txt", encoding='utf-8')
    source = file.readlines()



    #Take the list and construct a list of lists table
    #resembling the original table
    newSource = refineSource(source)
    enchantDict = enchantTableBuilder(newSource)
    return enchantDict
