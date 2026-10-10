class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l=0
        r=len(heights)-1
        max_count=0

        while l < r:
            lenght=min(heights[l],heights[r])
            weight=r-l
            cont=lenght*weight
            max_count= max(max_count, cont)
            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1
        return max_count           
        
        