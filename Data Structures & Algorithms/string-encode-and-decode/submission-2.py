class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        sz=[]
        sj=''
        for s in strs:
            sz.append(str(len(s)))
            sz.append(',')
        sz.append('#')
        sz.extend(strs)    
        
        return ''.join(sz) #not sure if this is a list or an string



    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i=0
        size=[]
        res=[]
        while s[i] != '#':
            j=i
            while s[j] !=',':
                j+=1
            size.append(int(s[i:j]))
            i= j+1
        i+=1
        for k in size:
            res.append(s[i:i+k])  
            i+=k 
        return res         