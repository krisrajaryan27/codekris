# https://leetcode.com/problems/contains-duplicate-ii/
class Solution: 
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create a dictionary which will store the last index of the number
        nums_index = {}
        for i, num in enumerate(nums):
            if num in nums_index and abs(i - nums_index[num]) <= k:
                return True
            nums_index[num] = i
        return False
        