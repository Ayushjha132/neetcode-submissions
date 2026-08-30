class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""
        
        res = "" # to store val
        l, r = 0, len(self.store[key]) - 1
        while l <= r:
            m = l + (r-l)//2
            if self.store[key][m][0] <= timestamp:
                l = m + 1
                res = self.store[key][m][1] # store prev value
            else:
                r = m - 1
        
        return res

        
        
