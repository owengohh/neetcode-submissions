class WordDictionary:

    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str) -> None:
        dictionary = self.dictionary
        for ch in word:
            if ch not in dictionary:
                dictionary[ch] = {}
            dictionary = dictionary[ch]
        dictionary["#"] = True

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return "#" in node
            
            char = word[idx]
            if char == ".":
                for key in node:
                    if key != '#' and dfs(node[key], idx+1):
                        return True
                return False
            else:
                if char in node:
                    return dfs(node[char], idx+1)
                else:
                    return False
    
        return dfs(self.dictionary, 0)
        
