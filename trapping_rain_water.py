heights = [0,1,0,2,1,0,1,3,2,1,2,1]

def get_total_water(height):
    """
    1. get left max array
    2. get right max array from the end
    3. minheight = min(left_max, right_max)
    4. water += (minheight - height) if height < minheight else 0
    """
    left_max = []
    temp_left_max = 0
    total_water = 0
    for i in height:
        left_max.append(temp_left_max)
        if i > temp_left_max:
            temp_left_max=i
    temp_right_max = 0
    right_max = list(range(len(height)))
    for index in reversed(range(len(height))):
        right_max[index] = temp_right_max
        temp_right_max = max(height[index], temp_right_max)
    for ele in range(len(height)):
        min_height = min(right_max[ele], left_max[ele])
        total_water += (min_height - height[ele]) if height[ele] < min_height else 0
    return total_water
        
        
    

print(get_total_water(heights))