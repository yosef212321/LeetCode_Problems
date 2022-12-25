class Solution:
    def fib(self, n: int) -> int:
        zero = 0 
        one = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            for i in range(n):
                temp = zero
                zero = one
                one = zero + temp
        return zero
        
