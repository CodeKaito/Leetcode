class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted_num = str(x)
        if converted_num[::-1] == converted_num: 
            return True
        else:
            return False
