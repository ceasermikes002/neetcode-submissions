class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n  # Store max height from the left for each bar
        right_max = [0] * n  # Store max height from the right for each bar
        total_water = 0
        
        # Calculate left max for each bar
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # Calculate right max for each bar
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        # Compute the trapped water
        for i in range(n):
            total_water += min(left_max[i], right_max[i]) - height[i]
        
        return total_water