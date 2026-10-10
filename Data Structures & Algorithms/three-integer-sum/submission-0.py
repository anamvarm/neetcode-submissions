class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        out=[]
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            if i > 0 and nums[i]== nums[i-1]:
                continue

            

            while j<k:
                val= nums[i]+nums[k]+ nums[j]
                if val==0 :
                    out.append([nums[i], nums[k], nums[j]])
                    j+=1
                    while nums[j]==nums[j-1] and j < k:
                        j+=1

                elif val<0:    
                    j+=1
                else:
                    k-=1

        return out                
        