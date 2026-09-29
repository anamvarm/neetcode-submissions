class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) < k:
            return ""

        dic=defaultdict(list)
        for num in nums:
            dic[num]=1+dic.get(num,0)  

        ver=[]    
        for num,cnt in dic.items():
            ver.append([cnt,num])
        ver.sort()  

        res=[]

        while len(res)<k:
            res.append(ver.pop()[1])

        return res      
        