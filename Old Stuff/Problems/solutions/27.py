def canFinish(numCourses: int, prerequisites: list[list[int]]) -> tuple[bool, list[int]]:
    # Create adjacency list for the graph
    graph = [[] for _ in range(numCourses)]
    for end_course, start_course in prerequisites:
        graph[start_course].append(end_course)

    visited = [False] * numCourses
    rec_stack = [False] * numCourses
    #3 -> 0 ->1 ->2 but dfs starts at 0, this is why rec_stack is useful
    # Also if undirected then rec_stack is useless
    sorted_vertices = []

    def dfs(vertex):
        visited[vertex] = True
        rec_stack[vertex] = True

        for adj_v in graph[vertex]:
            if not visited[adj_v]:
                if not dfs(adj_v): 
                    return False
            elif rec_stack[adj_v]: 
                return False
        
        rec_stack[vertex] = False
        sorted_vertices.append(vertex)
        return True

    for course in range(numCourses):
        if not visited[course]:
            if not dfs(course):
                return False, []

    return True, sorted_vertices[::-1]