class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        w_dict = defaultdict(list)
        for s in strs:
            s_sorted = "".join(sorted(s))
            w_dict[s_sorted].append(s)
        return [v for v in w_dict.values()]
