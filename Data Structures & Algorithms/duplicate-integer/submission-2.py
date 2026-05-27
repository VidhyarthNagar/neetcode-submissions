class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        monkey=set()
        for i in nums:
            if i not in monkey:
                monkey.add(i)
                
            else:
                return True
        return False
                


        