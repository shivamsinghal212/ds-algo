class MinHeap:
    def __init__(self):
        self.heap = []
    
    def swap(self, heap, ele1, ele2):
        heap[ele1], heap[ele2] = heap[ele2], heap[ele1]
        
    def add(self, value):
        value = int(value)
        self.heap.append(value)
        self.percolate_up(self.heap, len(self.heap)-1)
        
    def get_root(self):
        return self.heap[0]
        
    def pop(self):
        self.swap(self.heap, 0, len(self.heap)-1)
        popped = self.heap.pop()
        self.percolate_down(self.heap, 0)
        return popped
    
    def delete(self, value):
        temp_index = 0
        value = int(value)
        if len(self.heap) == 0:
            return
        if value not in self.heap:
            return
        for ele in self.heap:
            if ele == value:
                self.swap(self.heap, temp_index, len(self.heap)-1)
                self.heap.pop()
                break
            temp_index += 1
        self.percolate_down(self.heap, 0)
    
            
    def percolate_down(self, heap, index):
        child_index = (2 * index) + 1
        if child_index >= len(heap):
            return
        if child_index + 1 < len(heap) and heap[child_index+1] < heap[child_index]:
            child_index += 1
        if heap[child_index] < heap[index]:
            self.swap(heap, index, child_index)
            self.percolate_down(heap, child_index)
    
    def percolate_up(self, heap, index):
        parent_index = (index-1)//2
        if parent_index < 0:
            return
        if heap[index] < heap[parent_index]:
            self.swap(heap, index, parent_index)
            self.percolate_up(heap, parent_index)
            
    def heapify(self, arr):
        for ele in arr:
            self.add(ele)
        return self.heap
    
    def get_data(self):
        return self.heap
    
    def get_min(self):
#         print(self.heap[0])
        return self.heap[0]
#         
# obj = MinHeap()
# print(obj.heapify([1,3,-1, 0, 2, 4, 5, 8]))
# print(obj.pop())
# print(obj.get_data())
        
# imps = []
# no_of_inputs = int(input())
# for ele in range(no_of_inputs):
#     temp = input()
#     inner_ele = temp.split(' ')
#     imps.append(inner_ele)
# 
# obj = MinHeap()
# obj.add(4)
# obj.add(9)
# obj.get_min()
# obj.delete(4)
# obj.get_min()
# 
# 
# obj.get_data()
# for inp in imps:
#     if int(inp[0]) == int('1'):
#         obj.add(inp[1])
#     elif int(inp[0]) == int('2'):
#         obj.delete(inp[1])   
#     else:
#         obj.get_min()
        


        