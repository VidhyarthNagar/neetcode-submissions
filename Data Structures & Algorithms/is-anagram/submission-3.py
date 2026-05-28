class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            for i in s:
                x=s.count(i)
                if i in t:
                    b=t.count(i)
                    if x==b:
                        continue
                    else:
                        return False
                else:
                    return False
                return True
        else:
            return False
        return True
