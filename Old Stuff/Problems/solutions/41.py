def course_schedule(n, tasks: list[list[int]]):
    graph = [[] for _ in range(n)]
    for end_course, start_course in tasks:
        graph[start_course].append(end_course)
    
    visited = set()       
    rec_stack = set()      
    sorted_courses = []   

    def dfs(vertex):
        if vertex in rec_stack: 
            return False
        if vertex in visited:  
            return True
        
        rec_stack.add(vertex)
        
        for adj_v in graph[vertex]:
            if not dfs(adj_v):
                return False
        
        rec_stack.remove(vertex)
        visited.add(vertex)
        sorted_courses.append(vertex)
        
        return True
    
    for vertex in range(n):
        if vertex not in visited:
            if not dfs(vertex):
                return []  
    
    return sorted_courses[::-1]

tasks = [[1, 0], [2, 0], [3, 1], [3, 2]]
n = 4
print(course_schedule(n, tasks))
# Output: [0, 1, 2, 3] or [0, 2, 1, 3]
