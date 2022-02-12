#COMPLETE 
class U2016:
    #we pick the highest number and match with lowest number
    numSocks = int(input())
    socks = []

    #puts socks into array
    for i in range(numSocks):
        socks.append(int(input()))

    count = 0
    while (len(socks) != 0 and len(socks) != 1): 
        maxSock = max(socks); #we cant have these be the same sock

        maxIndex = socks.index(maxSock)

        minSock = socks[0]
        for sock in socks: 
            if sock < minSock and socks[maxIndex] != sock:
                minSock = sock

        minIndex = socks.index(minSock)
        
        socks[maxIndex] = maxSock - 1
        socks[minIndex] = minSock - 1

        if(socks[maxIndex] == 0) :
            socks.pop(maxIndex)

        #print(minIndex)
        if(socks[minIndex] == 0) :
            socks.pop(minIndex)
        
        count += 1
    print(count)
    
