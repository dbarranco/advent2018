
def countCharacters(x, boxes):
    chars = list(set(x)) #Get the different characters in the string received
    countedDoubleChar = False
    countedTripleChar = False

    for i in chars:
        occurences = x.count(i)

        if occurences == 2 and countedDoubleChar == False:
            countedDoubleChar = True
        if occurences == 3 and countedTripleChar == False:
            countedTripleChar = True

    if countedDoubleChar or countedTripleChar:
        boxes.append(x.rstrip('\n')) # Append trimmed string


    return countedDoubleChar, countedTripleChar

# Comparing two different strings
def similarStrings(s1, s2):
    count_diffs = 0
    for a, b in zip(s1, s2):
        if a!=b:
            if count_diffs: 
                return False
            count_diffs += 1
            
    return True

def main():
    # Initialise solution counters
    doubleCharCounter = 0 # For strings that have chars repeated twice
    tripleCharCounter = 0 # For strings that have chars repeated three times
    boxes = []

    f= open('input.txt', 'r')
    content= f.readlines()
    
    for x in content: 
        containsDouble, containsTriple = countCharacters(x, boxes)
        if containsDouble:
            doubleCharCounter += 1
        if containsTriple:
            tripleCharCounter += 1
    f.close()
    

    for stringA in boxes:
        for stringB in boxes:
            if stringA == stringB:
                break
            elif (similarStrings(stringA, stringB)):
                print("Found two strings that differ in a char.")
                print(stringA)
                print(stringB)
                #print("Common chars between strings:", set(stringA).intersection(set(stringB)) )

if __name__== "__main__":
  main()
