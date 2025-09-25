#Anagram -- algorithm to check if two words or phrase are anagrams or not

def anagram(str1, str2):
    #first check if length is same
    if len(str1) != len(str2):
        return False

    #Sort alphabetic both string
    str1 = sorted(str1)
    str2 = sorted(str2)

    print(str1)
    print(str2)

    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True


str1 = 'flustel'
str2 = 'restful'

print(anagram(str1, str2))