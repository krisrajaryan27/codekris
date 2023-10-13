#https://leetcode.com/problems/valid-anagram/
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        # Create dictionaries to store the character counts
        s_count = {}
        t_count = {}
        
        # Count the characters of string s
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        
        # Count the characters of string t
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
            
        return s_count == t_count
        
        
