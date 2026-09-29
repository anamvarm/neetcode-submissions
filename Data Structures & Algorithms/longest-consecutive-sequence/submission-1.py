class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

       longest=0
       setnums=set(nums)

       for num in setnums:
        if num - 1 not in setnums:
            length= 1
            while num + length in setnums:
                length+=1
            longest= max(length,longest)

       return longest         

        
        


        