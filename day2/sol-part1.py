
def countCharacters(x):
    chars = list(set(x)) #Get the different characters in the string received
    countedDoubleChar = False
    countedTripleChar = False

    for i in chars:
        occurences = x.count(i)

        if occurences == 2 and countedDoubleChar == False:
            countedDoubleChar = True
        if occurences == 3 and countedTripleChar == False:
            countedTripleChar = True

    return countedDoubleChar, countedTripleChar

def main():
    # Initialise solution counters
    doubleCharCounter = 0 # For strings that have chars repeated twice
    tripleCharCounter = 0 # For strings that have chars repeated three times

    f= open('input.txt', 'r')
    content= f.readlines()
    
    for x in content: 
        containsDouble, containsTriple = countCharacters(x)
        if containsDouble:
            doubleCharCounter = doubleCharCounter + 1
        if containsTriple:
            tripleCharCounter = tripleCharCounter + 1
    f.close()
    
    print("Counter for chars that are repeated twice is:", doubleCharCounter)
    print("Counter for chars that are repeated three times is:", tripleCharCounter)
    print("Checksum:", doubleCharCounter * tripleCharCounter)


if __name__== "__main__":
  main()
