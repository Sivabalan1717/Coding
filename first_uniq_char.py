class Solution(object):
    def firstUniqChar(self, s):
        has = {}

        for ch in s:
            if ch in has:
                has[ch] += 1
            else:
                has[ch] = 1

        for i in range(len(s)):
            if has[s[i]] == 1:
                return i

        return -1
