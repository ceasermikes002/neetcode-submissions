class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialise empty pre and postfix array
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)

        # initiase boundaries
        prefix[0] = 1
        postfix[len(nums) - 1] = 1

        prod1 = 1
        prod2 = 1

        for i in range(1, len(nums)):
            prod1 = prod1 * nums[i - 1]
            prefix[i] = prod1

        for i in range(len(nums)-2, -1, -1):
            prod2 = prod2 * nums[i + 1]
            postfix[i] = prod2

        final = []

        for i in range(len(nums)):
            final.append(prefix[i] * postfix[i])
        return final         