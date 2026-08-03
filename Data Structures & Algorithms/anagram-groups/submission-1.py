class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=[]
        fin={}
        for i in strs:
            if "".join(sorted(i)) not in x:

                x.append(("".join(sorted(i))))
                fin["".join(sorted(i))]=[]
                fin["".join(sorted(i))].append(i)
            else:
                fin["".join(sorted(i))].append(i)
            
            
        return list(fin.values())
        


        
        