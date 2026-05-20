class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """mul = int(num1) * int(num2)
        return str(mul)"""

        if num1 == "0" or num2 == "0": return "0"
        m,n = len(num1), len(num2)
        res = [0] * (m+n)

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                d1 = ord(num1[i])-ord('0')
                d2 = ord(num2[j])-ord('0')
                mult = d1*d2

                pos_low = i+j+1
                pos_high = i+j

                sum_val = mult + res[pos_low]
                res[pos_low] = sum_val % 10
                res[pos_high] += sum_val // 10
        result = []
        leading = True
        for digit in res:
            if digit == 0 and leading: continue
            leading = False
            result.append(str(digit))
        return ''.join(result) if result else "0"