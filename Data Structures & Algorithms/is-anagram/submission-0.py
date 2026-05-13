class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        combinedString = s+t
        HashDictForS = {}
        HashDictForCombined = {}
        for i in range(len(s)):
            if s[i] in HashDictForS:
                HashDictForS[s[i]]+=1
            else:
                HashDictForS[s[i]]=1
        for i in range(len(combinedString)):
            if combinedString[i] in HashDictForCombined:
                HashDictForCombined[combinedString[i]]+=1
            else:
                HashDictForCombined[combinedString[i]]=1
        if len(HashDictForS) != len(HashDictForCombined) and HashDictForS.keys() != HashDictForCombined.keys():
            return False
        for i in HashDictForS:
            if HashDictForCombined[i] != 2*HashDictForS[i]:
                return False
        return True