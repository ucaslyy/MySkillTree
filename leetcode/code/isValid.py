class Solution:
    def isValid(self, s: str) -> bool:
        """
        解决方案一：遍历所有符号，若为左括号，直接添加末尾；
                             若为右括号，则进一步判断是否有做括号可以匹配，若有则消除一对括号，
                                                                   若没有则返回false。
                  需要注意的是，在右扩号的场景中，此时如果stack为空，则stack[-1]会报错。当所有扩容都可以匹配上，才返回true。
        :param s:
        :return:
        """
        stack = []
        left_brackets = {"(", "[", "{"}
        right_brackets = {")": "(", "]": "[", "}": "{"}
        for item in s:
            if item in left_brackets:
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                if right_brackets[item] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
