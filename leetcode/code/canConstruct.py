class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        该题可以等价于字符串1中的所有字符都可以在字符串2中找到，且字符串1中字符出现的此数小于等于字符串2中出现的此数
        :param ransomNote:
        :param magazine:
        :return:
        """
        tmp1 = {}
        for i in range(len(ransomNote)):
            tmp1[ransomNote[i]] = 1 if ransomNote[i] not in tmp1 else tmp1[ransomNote[i]] + 1

        tmp2 = {}
        for i in range(len(magazine)):
            tmp2[magazine[i]] = 1 if magazine[i] not in tmp2 else tmp2[magazine[i]] + 1

        for key in tmp1.keys():
            if key not in tmp2 or tmp1[key] > tmp2[key]:
                return False

        return True
