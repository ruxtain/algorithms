class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        result = []
        while True:
            for word in strs:
                if not result:
                    try:
                        result.append(word[i])
                    except IndexError:
                        break
                else:
                    if word[i] == result[-1]:
                        pass
                    else:
                        result.pop()
            i += 1

        return ''.join(result)



Solution().longestCommonPrefix(["flower","flow","flight"])