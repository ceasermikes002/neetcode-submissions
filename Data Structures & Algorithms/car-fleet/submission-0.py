from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Start by creating tuples of position and speed for each car
        cars = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)
        
        # Initialize the list for times taken by each car to reach the target
        times = []
        
        for p, s in cars:
            # Calculate time for each car to reach the target
            current_time = (target - p) / s
            # Add to the times list
            times.append(current_time)
        
        # Start with zero fleets
        fleets = 0
        
        while times:
            # The lead car creates a new fleet
            lead_time = times.pop(0)
            fleets += 1
            
            # Continue popping out cars that form a fleet with the lead car
            while times and times[0] <= lead_time:
                times.pop(0)
        
        return fleets