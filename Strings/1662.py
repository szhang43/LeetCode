def equalString(word1, word2): 
    a = ""
    b = ""
    for i in range(len(word1)): 
        a += word1[i]
    for i in range(len(word2)): 
        b += word2[i]
    if a == b: 
        return True 
    return False


word1 = ["ab", "c"]
word2 = ["a", "bc"]

equalString(word1, word2)

word3 = ["a", "cb"], 
word4 = ["ab", "c"]

equalString(word3, word4)