class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            if carry == 0: return digits
        if carry: digits.insert(0,1)
        return digits