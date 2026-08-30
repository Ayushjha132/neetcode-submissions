class MyHashSet:

    def __init__(self):
        self.room = [[] for _ in range(1000)]
        self.size = 1000
    def add(self, key: int) -> None:
        pos = key % self.size
        if key not in self.room[pos]:
            self.room[pos].append(key)

    def remove(self, key: int) -> None:
        pos = key % self.size
        if key in self.room[pos]:
            self.room[pos].remove(key)

    def contains(self, key: int) -> bool:
        pos = key % self.size
        if key in self.room[pos]:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)