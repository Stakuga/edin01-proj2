import os

path_to_script = os.path.dirname(os.path.realpath(__file__))

def digitToString(b1, b2, b3, b4):
    output = str(b1) + str(b2) + str(b3) + str(b4)
    return(output)

def digitMap(a, b):
    if a == 0 and b == 0:
        return("0")
    elif a == 0 and b == 1:
        return("1")
    elif a == 0 and b == 2:
        return("2")
    elif a == 0 and b == 3:
        return("3")
    elif a == 0 and b == 4:
        return("4")
    elif a == 1 and b == 0:
        return("5")
    elif a == 1 and b == 1:
        return("6")
    elif a == 1 and b == 2:
        return("7")
    elif a == 1 and b == 3:
        return("8")
    elif a == 1 and b == 4:
        return("9")

def digitOut(a1, a2, a3, a4, b1, b2, b3, b4):
    output = digitMap(a1, b1) + digitMap(a2, b2) + digitMap(a3, b3) + digitMap(a4, b4)
    return(output)

def modTwo(a1, a2, a3, a4):

    listOfCombos = []
    firsts = ""

    listOfCombos.append(digitToString(a1, a2, a3, a4))
    firsts = firsts + str(a1)

    foundAMatch = False

    while foundAMatch == False:

        aNewDigit = (a3 + a4) % 2
        a4 = a3
        a3 = a2
        a2 = a1
        a1 = aNewDigit

        newCombo = digitToString(a1, a2, a3, a4)
        if newCombo in listOfCombos:
            foundAMatch = True
        else:
            listOfCombos.append(newCombo)
            firsts = firsts + newCombo[0]
    listOfCombos.append("0000")
    firsts = firsts + "0"
    return((listOfCombos, firsts))

def modFive(a1, a2, a3, a4):
    
    listOfCombos = []
    firsts = ""

    listOfCombos.append(digitToString(a1, a2, a3, a4))
    firsts = firsts + str(a1)

    foundAMatch = False

    while foundAMatch == False:

        aNewDigit = (a1 + a2 * 2 + a4 * 2) % 5
        a4 = a3
        a3 = a2
        a2 = a1
        a1 = aNewDigit

        newCombo = digitToString(a1, a2, a3, a4)
        if newCombo in listOfCombos:
            foundAMatch = True
        else:
            listOfCombos.append(newCombo)
            firsts = firsts + newCombo[0]
    listOfCombos.append("0000")
    firsts = firsts + "0"
    return((listOfCombos, firsts))

modTwoList, firstsTwo = modTwo(0, 0, 0, 1)[0], modTwo(0, 0, 0, 1)[1]
modFiveList, firstsFive = modFive(0, 0, 0, 1)[0], modFive(0, 0, 0, 1)[1]

##############################

duplicate = False

digits = []
leftIndex = 0
rightIndex = 0

while duplicate == False:
    leftCombo = modTwoList[leftIndex]
    rightCombo = modFiveList[rightIndex]

    a1 = int(leftCombo[0])
    a2 = int(leftCombo[1])
    a3 = int(leftCombo[2])
    a4 = int(leftCombo[3])
    b1 = int(rightCombo[0])
    b2 = int(rightCombo[1])
    b3 = int(rightCombo[2])
    b4 = int(rightCombo[3])

    unifiedCombo = digitOut(a1, a2, a3, a4, b1, b2, b3, b4)
    
    if unifiedCombo in digits:
        duplicate = True
    
    digits.append(unifiedCombo)

    leftIndex = leftIndex + 1
    
    if leftIndex % 16 == 0:
        leftIndex = 0
    
    rightIndex = rightIndex + 1
    
    if rightIndex % 625 == 0:
        rightIndex = 0
debruijn = ""
for i in digits:
    debruijn = debruijn + i[0]

finale = "00" + debruijn

output_file = os.path.join(path_to_script, "debruijn.txt")

output_file = open(output_file, "w")
n = output_file.write(finale)
output_file.close()