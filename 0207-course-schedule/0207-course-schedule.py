class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        q=deque()
        indegree=[0]*numCourses
        for i in range(numCourses):
            for j in adj[i]:
                indegree[j]+=1
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        cnt=0
        while q:
            n=q.popleft()
            cnt+=1
            for i in adj[n]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        return cnt==numCourses
        