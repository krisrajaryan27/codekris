# https://leetcode.com/problems/contains-duplicate-iii/
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False
        
        num_index = {}  # Dictionary to store the last seen value's index
        
        for i, num in enumerate(nums):
            # Calculate the bucket for the current number
            bucket = num // (valueDiff + 1)

            # Check if the current bucket or adjacent buckets have numbers that meet the conditions
            if bucket in num_index or (bucket - 1 in num_index and abs(num - num_index[bucket - 1]) <= valueDiff) or (bucket + 1 in num_index and abs(num - num_index[bucket + 1]) <= valueDiff):
                return True

            # Remove entries that are too far away (indexDiff constraint)
            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // (valueDiff + 1)
                del num_index[old_bucket]

            num_index[bucket] = num

        return False