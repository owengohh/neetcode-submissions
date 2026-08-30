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
        def dfs(trie, i):
            if i == len(word):
                return "#" in trie
            if word[i] == '.':
                for key in trie:
                    if key != '#' and dfs(trie[key], i+1):
                        return True
                    else:
                        return False
            else:
                if word[i] not in trie:
                    return False
                else:
                    return dfs(trie[word[i]], i+1)
        
        return dfs(self.trie, 0)