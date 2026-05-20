class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tx,ty,tz = target
        maxX = maxY = maxZ = 0

        for x,y,z in triplets:
            if x <= tx and y <= ty and z <= tz:
                maxX = max(maxX,x)
                maxY = max(maxY,y)
                maxZ = max(maxZ,z)
        return [maxX,maxY,maxZ] == target