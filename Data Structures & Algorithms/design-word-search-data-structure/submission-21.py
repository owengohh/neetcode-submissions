class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for ch in word:
            trie = trie.setdefault(ch, {})  # simpler than if-not-in
        trie["#"] = True  # marks end of word

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "#" in node

            ch = word[i]
            if ch == ".":
                # check all branches — cannot return early unless True is found
                return any(
                    key != "#" and dfs(node[key], i + 1) for key in node
                )
            if ch not in node:
                return False
            return dfs(node[ch], i + 1)

        return dfs(self.trie, 0)
        