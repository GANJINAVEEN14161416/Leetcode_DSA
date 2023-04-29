class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node
        dic={}
        def dfs(node):
            if node in dic:
                return dic[node]
            copy=Node(node.val)
            dic[node]=copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node)