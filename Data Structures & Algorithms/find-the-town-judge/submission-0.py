class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1 and not trust:
            return 1
            
        # assuming everyone (1 to n) trusts no one
        notTrust = set(range(1, n + 1))
        
        # Track how many people trust each person
        trusted_count = [0] * (n + 1)

        for a, b in trust:
            # Person 'a' trusts someone, so they cannot be the judge
            if a in notTrust:
                notTrust.discard(a)
            
            # Count how many people trust person 'b'
            trusted_count[b] += 1
        
        # The judge must be someone who trusts no one AND is trusted by everyone else (n - 1 people)
        for person in notTrust:
            if trusted_count[person] == n - 1:
                return person
        
        return -1