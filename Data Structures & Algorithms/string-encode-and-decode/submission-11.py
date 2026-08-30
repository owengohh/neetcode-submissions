class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
        # find the position of the delimiter "#"
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # extract the string
            word = s[j+1:j+1+length]
            res.append(word)

            # move to the start of the next encoded string
            i = j + 1 + length
        
        return res
