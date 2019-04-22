'''

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''


class Solution(object):
    def strStr(self, haystack, needle):
        # 水题，不想写
        return haystack.find(needle)



if __name__ == '__main__':
    s = Solution()
    print(s.strStr("aaaaa", "bba"))

