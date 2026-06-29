class Solution:
    def checkRecord(self, s: str) -> bool:
        a=0
        l=0
        for word in s:
            if word=='A':
                a+=1
        if a>=2:
            return False
        if 'LLL' in s:
            return False
        return True
            
        
