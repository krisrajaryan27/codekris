#https://leetcode.com/problems/contains-duplicate/
"""
Check if the given list of integers contains any duplicates.
    Parameters:
        nums (List[int]): A list of integers.
    Returns:
        bool: True if the list contains duplicates, False otherwise.
"""
class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool :
        hashSet = set()
        for num in nums :
            if num in hashSet :
                return True
            hashSet.add(num)
        return False