class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}
        res = 0
        for ch in s:
            hashmap[ch] = hashmap.get(ch, 0) + 1
            if hashmap[ch] % 2 == 0:
                res += 2
                
        for cnt in hashmap.values():
            if cnt % 2:
                res += 1
                break
        
        return res
