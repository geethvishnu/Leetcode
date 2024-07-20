class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        strs.sort()
        anagramd ={}
        for i in strs:
            sortedString = str(sorted(i))
            if sortedString not in anagramd:
                anagramd[sortedString] = [i]
            else:
                anagramd[sortedString].append(i)
        return list(anagramd.values())
        
        