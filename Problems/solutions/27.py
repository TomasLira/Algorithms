def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # Create adjacency list
    adj_list = {i: [] for i in range(numCourses)}
    for end_course, start_course in prerequisites:
        # To do end_course, we need to do start_course first
        adj_list[start_course].append(end_course) 

    visited = set()
    # Set to track nodes in the current recursion stack (path)
    # node wasnt fully processed, therefore has a cycle
    recStack = set()
    
    def dfs(course):
        # if is in the current path then back edge
        if course in recStack:
            return False
        # course is fully processed
        if course in visited:
            return True

        # Mark the course as visited and add to recursion stack
        visited.add(course)
        recStack.add(course)
        
        for adj_course in adj_list[course]:
            # if all courses `adj_course` can be completed, then return True else False
            if not dfs(adj_course):
                return False
        recStack.remove(course)
        return True 
    
    for course in range(numCourses):
        if course not in visited:
            if not dfs(course):
                return False
    return True
