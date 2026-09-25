class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sz=[]
        for s in strs:
            sz.append(str(len(s)))
            sz.append(',')
        sz.append('#')
        sz.extend(strs)
        return ''.join(sz)    


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sz,res=[],[]
        i=0
        while s[i] != '#':
            j=i
            while s[j] != ',':
                j+=1
            sz.append(int(s[i:j]))
                
            i= j+1

        i+=1
        for di in sz:
            res.append(s[i:i+di])
            i+=di

        return  res