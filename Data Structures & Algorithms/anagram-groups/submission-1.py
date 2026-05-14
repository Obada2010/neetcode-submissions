class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == []:
            return [[""]]
        anagramMap = {}
        for i in range(len(strs)):
            hashKeyArray = [0]*26
            for char in strs[i]:
                index = ord(char) - ord("a")
                hashKeyArray[index]+=1
            hashKeyTuple = tuple(hashKeyArray)
            if hashKeyTuple in anagramMap:
                anagramMap[hashKeyTuple].append(strs[i])
            else:
                anagramMap[hashKeyTuple] = [strs[i]]
        finalList = []
        for values in anagramMap.values():
            finalList.append(values)
        return finalList
        