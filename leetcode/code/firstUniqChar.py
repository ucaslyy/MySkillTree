class Solution:
    def firstUniqChar(self, s: str) -> int:
        tmp = {}
        for i in range(len(s)):
            if s[i] in tmp:
                tmp[s[i]][1] += 1
            else:
                tmp[s[i]] = [i, 1]

        ans = len(s)
        for key in tmp.keys():
            if tmp[key][1] == 1:
                ans = min(ans, tmp[key][0])

        return -1 if ans == len(s) else ans
