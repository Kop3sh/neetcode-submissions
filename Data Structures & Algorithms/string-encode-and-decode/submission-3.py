class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = []
        for s in strs:
            sentence.append(str(len(s)))
            sentence.append(":")
            sentence.append(s)
        
        return "".join(sentence)


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != ':':
                j += 1
            c = int(s[i:j])
            i = j + 1
            j = i + c
            res.append(s[i:j])
            i = j
        
        return res
