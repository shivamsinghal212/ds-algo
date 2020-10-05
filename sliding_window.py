from max_heap import MaxHeap

solution = []

def get_max_sliding_window(arr, window_start=0, window_end=3):
    window_arr = arr[window_start:window_end]
    heap_obj = MaxHeap()
    heap_obj.heapify(window_arr)
    min_ele = heap_obj.get_max()
    solution.append(min_ele)
    window_start += 1
    window_end += 1
    if window_end <= len(arr):
        get_min_sliding_window(arr, window_start, window_end)
        

class Solution:
    def __init__(self):
        self.solution = []
    def maxSlidingWindow(self, nums, k, window_start=0):
        window_arr = nums[window_start:k]
        heap_obj = MaxHeap()
        heap_obj.heapify(window_arr)
        max_ele = heap_obj.get_max()
        self.solution.append(max_ele)
        window_start += 1
        k += 1
        if k <= len(nums):
            self.maxSlidingWindow(nums, k, window_start)
        return self.solution

print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))

