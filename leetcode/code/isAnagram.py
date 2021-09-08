class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        该题可以等价于字符串1和字符2中的所有字符都可以在对方中找到，且字符串1中字符出现的次数等于字符串2中出现的此数
        :param s:
        :param t:
        :return:
        """
        tmp1 = {}
        for i in range(len(s)):
            tmp1[s[i]] = 1 if s[i] not in tmp1 else tmp1[s[i]] + 1

        tmp2 = {}
        for i in range(len(t)):
            tmp2[t[i]] = 1 if t[i] not in tmp2 else tmp2[t[i]] + 1

        for key in tmp1.keys():
            if key not in tmp2 or tmp1[key] != tmp2[key]:
                return False

        for key in tmp2.keys():
            if key not in tmp1 or tmp1[key] != tmp2[key]:
                return False

        return True
