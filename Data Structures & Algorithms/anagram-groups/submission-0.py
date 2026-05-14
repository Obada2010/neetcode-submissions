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
                anagramMap[hashKeyTuple].append(i)
            else:
                anagramMap[hashKeyTuple] = [i]
        finalList = []
        for keys in anagramMap:
            innerList = []
            for values in anagramMap[keys]:
                innerList.append(strs[values])
            finalList.append(innerList)
        return finalList
        