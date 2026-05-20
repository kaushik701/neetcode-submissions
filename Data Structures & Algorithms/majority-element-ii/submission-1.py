class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1,cand2 = None,None
        count1,count2 = 0,0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        res = []
        threshold = len(nums) // 3

        for cand in [cand1,cand2]:
            if cand is not None and nums.count(cand) > threshold:
                res.append(cand)
        return res
        
        """count = defaultdict(int)
        for n in nums:
            count[n] += 1

            if len(count) <= 2: continue
            new_count = defaultdict(int)
            for n,c in count.items():
                if c > 1:
                    new_count[n] = c-1
            count = new_count

        res = []
        for n in count:
            if nums.count(n) > len(nums) // 3: 
                res.append(n)
        return res"""



