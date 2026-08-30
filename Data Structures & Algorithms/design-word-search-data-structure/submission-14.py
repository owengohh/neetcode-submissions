class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            if ch not in trie:
                trie[ch] = {}
            trie = trie[ch]
        trie['#'] = {}

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node
            if word[i] == '.':
                for key in node:
                    if key != "#" and dfs(node[key], i+1):
                        return True
                return False
            else:
                ch = word[i]
                if ch not in node:
                    return False
                else:
                    return dfs(node[ch], i+1)
        
        return dfs(self.trie, 0)