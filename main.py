from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    def help(visited, frontier):
        # print(frontier)
        # print()
        # print('depth:', depth)
        # print(visited)
        if len(frontier) == 0:
            return visited
        else:
            distance, node, deep = heappop(frontier)
            # print(distance,node,deep)
            # print('visiting', node)
            if node in visited:
                # Already visited, so ignore this longer path
                return help(visited, frontier)
            else:
                # We now know the shortest path from source to node.
                # insert into visited dict.
                visited[node] = (distance, deep)
                # depth.append(node)
                # print('...distance=', distance)
                # Visit each neighbor of node and insert into heap.
                # We may add same node more than once, heap
                # will keep shortest distance prioritized.
                for neighbor, weight in graph[node]:
                    # print(neighbor, weight)
                    heappush(frontier, (distance + weight, neighbor, deep + 1))
                return help(visited, frontier)
        

    frontier = []
    heappush(frontier, (0, source, 0))
    visited = {}
    return help(visited, frontier)
    
graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 8), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }

# result = shortest_shortest_path(graph, 's')
# print(result)


def bfs_path(graph, source):
    visited = set()
    queue = deque([(source)])
    parents = {}

    while queue:
        node = queue.popleft()

        if node not in visited:
            # print(parents)
            # print('visiting',node)
            visited.add(node)
            # print(graph[node])
            # print(visited)
            for i in graph[node]:
                if i not in parents.keys():
                    parents[i] = node
            try:
                queue.extend(graph[node] - visited)
                # print(queue)
            except:
                pass
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    return {k: parents[k] for k in sorted(parents)}

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


print(bfs_path(get_sample_graph(),'s'))
    
def get_path(parents, destination):
    node = destination
    path = ''
    while node!= 's':
        path += node
        node = parents[node]
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    return (path[1:] + 's')[::-1]

parents = bfs_path(get_sample_graph(),'s')
print(get_path(parents, 'd'))

