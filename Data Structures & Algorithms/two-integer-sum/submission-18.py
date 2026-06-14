class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Initialize the hashmap
        hashmap = {}

        # Loop through nums array
        for i, num in enumerate(nums):
            complement = target - num
            # Check if complement is in hashmap
            if complement in hashmap:
                return[hashmap[complement], i]
            
            hashmap[num] = i
        