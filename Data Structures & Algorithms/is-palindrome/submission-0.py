class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return True

        s = s.lower()
        
        alphabet = [
            'a', 'b', 'c', 'd', 'e', 
            'f', 'g', 'h', 'i', 'j', 
            'k', 'l', 'm', 'n', 'o', 
            'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 
            'z', 
            '0', '1', '2', '3', 
            '4', '5', '6', '7', 
            '8', '9'
        ]

        s_list = []
        list_size = 0

        for c in s:
            if c in alphabet:
                list_size += 1
                s_list.append(c)

        r = list_size - 1
        for l in range(list_size // 2):
            if s_list[l] != s_list[r]:
                return False
            r -= 1
        
        return True