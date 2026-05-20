class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalTank = 0
        currTank = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            totalTank += gain
            currTank += gain

            if currTank < 0:
                start = i+1
                currTank = 0
        
        if totalTank < 0: return -1

        return start