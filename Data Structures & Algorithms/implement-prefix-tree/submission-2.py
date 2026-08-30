class PrefixTree:

    def __init__(self):
        self.prefix_tree = {}

    def insert(self, word: str) -> None:
        curr = self.prefix_tree
        for ch in word:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]
        curr['.'] = {}

    def search(self, word: str) -> bool:
        curr = self.prefix_tree
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
        return "." in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.prefix_tree
        for ch in prefix:
            if ch not in curr:
                return False
            curr = curr[ch]
        return True