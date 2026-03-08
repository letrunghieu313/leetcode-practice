# Regular brute force appoach where we seach for the correct matching char,
# if not, we return False immediately 
def canConstruct(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    myMagazineList = list(magazine)

    for ch in ransomNote:
        found = False

        for i in range(len(myMagazineList)):
            if myMagazineList[i] == ch:
                found = True
                myMagazineList.pop(i)   # remove used letter
                break                  # stop searching

        if not found:
            return False   # letter not found at all

    return True
            
# TC: O(n.m)       
# SC: O(m)     


# Dictionary (HashMap) when you deal with frequency of something,
# New learning that: we do not need to loop through string by index, 
# just loop through it, and it can sort out by (for loop python function)
def canConstructV2(self, ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    my_map = {}

    # count letters in magazine
    for ch in magazine:
        my_map[ch] = my_map.get(ch, 0) + 1

    # use letters for ransomNote
    for ch in ransomNote:
        remaining = my_map.get(ch, 0)
        if remaining == 0:
            return False
        my_map[ch] = remaining - 1

    return True
            
# TC: O(m)       
# SC: O(k)   k <= 26 => O(1)
        
        
        




"""
2 strings: ransomNote and magazine:
+ true if ransomeNote can be contruced by using letter from magazine string
+ false otherwise
Each letter in magazine only use once in ransomNote

"""