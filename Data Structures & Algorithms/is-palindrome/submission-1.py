class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        st = []
        for c in s:
            if  ord('z') >= ord(c) >= ord('a') or ord('9') >= ord(c) >= ord('0'):
                st.append(c) 


        s = ''.join(st)
        n = len(s)
        l, r = 0, n - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        