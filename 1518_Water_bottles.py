numBottles=15
numExchange=8

maxDrank=0
emptyBottles=0

while True:
    maxDrank+=numBottles
    #print(maxDrank)
    emptyBottles+=numBottles
    #print(emptyBottles)
    em=emptyBottles
    numBottles=emptyBottles//numExchange
    #print(numBottles)
    emptyBottles=em%numExchange
    #print(emptyBottles)
    if (numBottles+emptyBottles)<numExchange:
        maxDrank+=numBottles
        break

print(maxDrank)