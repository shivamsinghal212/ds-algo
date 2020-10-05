from max_heap import MaxHeap
from min_heap import MinHeap

class MedianOfAStream:
    maxh_obj = MaxHeap()
    minh_obj = MinHeap()
    maxHeap = maxh_obj.get_data()
    minHeap = minh_obj.get_data()
    
    def insert_num(self, num):
        # if Max heap is empty or input is smaller than existing root of maxheap  
        if not self.maxHeap or num <= self.maxh_obj.get_root():
            self.maxh_obj.add(num)
        else:
            self.minh_obj.add(num)
        # balancing the two heaps
        
        #here we are assuming that maxheap can have one extra element
        if len(self.maxHeap) > len(self.minHeap) + 1:
            self.minh_obj.add(self.maxh_obj.pop())
        elif len(self.maxHeap) < len(self.minHeap):
            self.maxh_obj.add(self.minh_obj.pop())
            
    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (self.maxHeap[0]+ self.minHeap[0]) /2.0
        return self.maxHeap[0]/1.0
    

obj = MedianOfAStream()
obj.insert_num(3)
obj.insert_num(1)
print(obj.find_median())
obj.insert_num(5)
print(obj.find_median())
obj.insert_num(4)
print(obj.find_median())

