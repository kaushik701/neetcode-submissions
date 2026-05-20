class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(left,right):
            sortedArray = [None] * (len(left)+len(right))
            k = i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sortedArray[k] = left[i]
                    i += 1
                else:
                    sortedArray[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                sortedArray[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                sortedArray[k] = right[j]
                j += 1
                k += 1
            return sortedArray

        if len(nums) == 1: return nums
        middle = len(nums) //2
        left = nums[:middle]
        right = nums[middle:]
        return mergeSort(self.sortArray(left),self.sortArray(right))        
        """
        nums.sort()
        return nums
        """
         