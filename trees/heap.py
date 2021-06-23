class Heap():
    def __init__(self):
        self.data = ["#"]
        self.heapified = False

    def insert(self, value):
        self.data.append(value)
        self.heapify()
    
    def delete(self):
        self.data[1], self.data[-1] = self.data[-1], self.data[1]
        val = self.data.pop()
        self.heapify()
        return val

    def merge(self):
        pass

    def isLeaf(self, index):
        return 2 * index > len(self.data) - 1

    def heapify(self):

        n = len(self.data) - 1

        while n > 0:
            if not self.isLeaf(n):
                left_child = 2 * n
                right_child = (2 * n) + 1

                index = left_child
                if right_child < len(self.data) and self.data[right_child] > self.data[left_child]:
                    index = right_child
                    
                if self.data[n] < self.data[index]:
                    self.data[n], self.data[index] = self.data[index], self.data[n]
            
            n -= 1

h = Heap()
h.insert(1)
h.insert(96)
h.data
h.insert(3)
h.insert(4)
h.insert(10)
h.insert(40)
h.insert(56)

print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())
print(h.delete())




