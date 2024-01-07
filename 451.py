def frequencySort(s): 
    hashTable = {}
    for i in range(len(s)): # can also use for in ..
        if s[i] in hashTable: 
            hashTable[s[i]] += 1
        else: 
            hashTable[s[i]] = 1
    

print(frequencySort("tree"))

