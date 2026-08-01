from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create adjacency list and in-degree array for graph representation
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        # Fill graph and in-degree array
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1
        
        # Step 2: Collect courses with no prerequisites
        zero_degree_courses = [i for i in range(numCourses) if in_degree[i] == 0]
        
        # Step 3: Process courses with zero in-degree using a queue
        processed_courses = 0
        while zero_degree_courses:
            course = zero_degree_courses.pop()
            processed_courses += 1
            # Reduce the in-degree of the course's dependent courses
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                # If a course has in-degree reduced to zero, it means it can now be taken
                if in_degree[neighbor] == 0:
                    zero_degree_courses.append(neighbor)
        
        # Step 4: If all courses are processed, it means there's no cycle
        return processed_courses == numCourses