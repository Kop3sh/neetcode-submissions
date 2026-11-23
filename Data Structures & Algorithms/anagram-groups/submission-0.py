from collections import defaultdict

class Solution:
    def char_freq(self, word: str) -> dict:
        freq = [0] * 26
        for c in word:
            freq[ord(c) - ord('a')] += 1
        return freq

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = defaultdict(list)

        for s in strs:
            f = tuple(self.char_freq(s))
            freqs[f] = freqs.get(f, [])
            freqs[f].append(s)
        res = []
        for k, v in freqs.items():
            res.append(v)

        return res
