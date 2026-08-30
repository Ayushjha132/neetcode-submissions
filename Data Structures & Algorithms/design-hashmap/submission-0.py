# time O(1) and space O(1000000) even there is only item but very fast
# class MyHashMap:

#     def __init__(self):
#         self.room = [-1] * 1000000

#     def put(self, key: int, value: int) -> None:
#         self.room[key] = value

#     def get(self, key: int) -> int:
#         return self.room[key]

#     def remove(self, key: int) -> None:
#         self.room.pop(key)

# bucket approch 
# time O(1) space O()

class MyHashMap:

    def __init__(self):
        self.rooms = [[] for _ in range(1000)]
        self.size = 1000

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        room = self.rooms[index]
        # search the condition when key already there
        # can't do direct search need for loop with index position in one room
        for i, (k, v) in enumerate(room):
            if k == key:
                room[i] = (key, value)
                return
        room.append((key, value))

    def get(self, key: int) -> int:
        index = key % self.size
        room = self.rooms[index]
        # tupe can be direclty unwrap in for loop 
        # each each items inside the same list
        for k, v in room:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        room = self.rooms[index]

        for i, (k, v) in enumerate(room):
            if k == key:
                room.pop(i)
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)