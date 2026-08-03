class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i !=j and i<j:
                    a=[]
                    a.append(i)
                    a.append(j)
                    break
                elif i>j and nums[i]+nums[j]==target and i !=j:
                    a=[]
                    a.append(j)
                    a.append(i)
                    break
                
        return a      
        