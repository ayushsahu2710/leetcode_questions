class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0
        tLen = len(target)
        for i in range(1, n+1):
            ans.append( "Push" )
            if i < target[j]:
                ans.append( "Pop" )
            else:
                j+=1
                if j == tLen:
                    break
        return ans

