import string
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        cleanStr = ''.join(ch for ch in s if ch.isalnum())
        if not cleanStr or cleanStr.isspace():
            return True
        if (cleanStr == cleanStr[::-1]):
            return cleanStr
        """
        :type s: str
        :rtype: bool
        """
        