import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #return (n != 0) & ((n & (n - 1)) == 0)

        for P in range(0,32):
            if n == math.pow(2, P):
                return True


        