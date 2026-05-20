class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
         # Find the maximum drop-off location to determine array size
        maxLocation = max(trip[2] for trip in trips)

         # Difference array: diff[i] is net change of passengers at location i
        diff = [0] * (maxLocation+1)

         # apply each trips effect to the different array
        for num_passengers, start, end in trips:
            diff[start] += num_passengers # passengers get in at 'start'
            diff[end] -= num_passengers # passengers get out at 'end'

        curr_passengers = 0
        for change in diff:
            curr_passengers += change
            if curr_passengers > capacity:
                return False
        
        return True