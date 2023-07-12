class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        V=len(adj)
        q=deque()
        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        count=0
        ans=[]
        while q:
            x=q.popleft()
            count+=1
            ans.append(x)
            for child in adj[x]:
                indegree[child]-=1
                if indegree[child]==0:
                    q.append(child)
        return ans if count==numCourses else []
        