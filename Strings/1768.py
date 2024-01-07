def altMergeString1(word1, word2): 
    i, j = 0, 0
    result = ""
    w1 = len(word1)
    w2 = len(word2)

    if w1 == w2: #Check if the strings are equal
        for i in range(len(word1)): # Loop through the length of the words
            result += word1[i] + word2[j] # Append the index of i and j to the words to result 
            i+=1
            j+=1 # increment i and j to move along the two strings

            if i == w1: # Final check if it has reached the end 
                return result
    else:  # If the strings are different length
        if(w1 > w2): # if word 1 is larger than word 2
            for i in range(w2):
                result += word1[i] + word2[j]
                i+=1
                j+=1
            result += word1[i:] # add the remaining of word 1 to result 
        else:
            if(w1 < w2): # If word1 is less than word2
                for i in range(w1):
                    result += word1[i] + word2[j]
                    i+=1
                    j+=1
                result += word2[j:]
    return result # Return the final result 


def altMergeString2(word1, word2):
    i, j = 0, 0
    result = ""

    while i < len(word1) and j < len(word2): # Iterate until one word reached its end 
        result += word1[i] + word2[j] # Append the index of i and j of the words to result 
        i+=1
        j+=1
        # Increment the counter to move along the string
    result += word1[i:] + word2[j:] # Append the remaining of either strings 

    return result

