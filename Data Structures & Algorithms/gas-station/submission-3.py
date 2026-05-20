class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total < 0:
                total = 0
                res = i+1
        return res
        
        """
        totalTank = 0  # total gas - cost over the whole circle
        currTank = 0   # gas - cost from current start to current index
        start = 0      # candidate starting station

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            totalTank += gain
            currTank += gain

            # If we can't reach station i+1 from current start,
            # then start..i cannot be a valid starting segment.
            if currTank < 0:
                start = i + 1    # next station is new candidate
                currTank = 0     # reset current tank for new segment
        # If total gas is less than total cost, it's impossible
        if totalTank < 0: return -1

        return start"""