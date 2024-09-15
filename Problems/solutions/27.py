# Wrong answer
def largestRectangleArea(heights: list[int]) -> int: 
        min_height,base = heights[0],1
        max_rectangle = heights[0]
        for idx in range(1,len(heights)):
            min_height = min(min_height,heights[idx])
            if min_height*(base+1) > heights[idx]:
                base += 1
            else:
                base = 1
                min_height = heights[idx]
            max_rectangle = max(max_rectangle,base*min_height)
            print("---",max_rectangle)
        return max_rectangle
    
    
print(largestRectangleArea([1,2,3,4,5]))