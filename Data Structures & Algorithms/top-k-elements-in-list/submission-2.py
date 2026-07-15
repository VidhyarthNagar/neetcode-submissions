class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x={}
        for i in nums:
            if not i in x:
                x[i]=0
                x[i]+=1
            else:
                x[i]+=1
        a=0
        b=[]
        pairs = list(x.items())
        pairs.sort(key=lambda p: p[1], reverse=True)
        
        for i in range(k):
            b.append(pairs[i][0])
        return b
            


                
            



        