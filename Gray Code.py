class Solution:
    def grayCode(self, n: int) -> List[int]:
        #calculating how many elements we will have
        iters = 1 << n 
        ret = [0]*iters
        
        for y in range(iters):
            #easiest way to convert binary to gray
            ret[y] = y ^ (y>>1)

        return ret
