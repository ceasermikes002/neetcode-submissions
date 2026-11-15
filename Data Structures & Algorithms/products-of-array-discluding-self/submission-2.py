class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # initialize pre and postfix arrays
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)   

        # initialise boundary positions
        prefix[0] = 1
        postfix[len(nums) - 1] = 1

        prod1 = 1
        prod2 = 1

        # build prefix array from left to right
        for i in range(1, len(nums)):
            prod1 = prod1 * nums[i - 1]
            prefix[i] = prod1
        
        # build postfix array
        for i in range(len(nums) -2, -1, -1):

            prod2 = prod2 * nums[i + 1]
            postfix[i] = prod2
        
        final = []

        for i in range(len(nums)):
            final.append(prefix[i] * postfix[i])
        return final        