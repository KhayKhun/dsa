class MyHashMap:

    def __init__(self):
        self.values = []

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.values)):
            if self.values[i][0] == key:
                self.values[i][1] = value
                return
        self.values.append([key,value])


    def get(self, key: int) -> int:
        for i in self.values:
            if i[0] == key: return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.values)):
            if self.values[i][0] == key: 
                self.values.remove(self.values[i])
                return
        return -1
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)