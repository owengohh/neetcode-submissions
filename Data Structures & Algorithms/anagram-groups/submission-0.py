class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)

        for s in strs:
            list_s = sorted(list(s))
            anagramMap["".join(list_s)].append(s)
        
        return list(anagramMap.values())