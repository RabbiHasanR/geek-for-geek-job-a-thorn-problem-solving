from typing import List

class Solution:
    def solve(self, N : int, a : int , x : List[int]) -> int:
        x = sorted(x)
        if len(x) < 4:
            elements = x
        else:
            elements = [x[0],x[1],x[N-2], x[N-1]]
        result = 0
        for i in range(len(elements)):
            for j in range(i+1,len(elements)):
                s = abs(a - elements[i]) + abs(a - elements[j])
                result = max(result, s)
        return result


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N,A = [int(i) for i in input().split()]
        
        
        X = [int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.solve(N,A,X)
        
        print(res)
# } Driver Code Ends