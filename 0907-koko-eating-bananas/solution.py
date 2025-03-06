class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(piles,speed,h):
            total=0
            for bananas in piles:
                total+=(bananas//speed)
                if bananas%speed!=0:
                    total+=1

            return total<=h

        left,right=1,max(piles)

        while left<right:
            mid=(left+right)//2
            if canEat(piles,mid,h):
                right=mid
            else:
                left=mid+1
        return left
