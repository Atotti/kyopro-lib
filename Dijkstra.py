from typing import List, Tuple, Dict
import heapq

class Graph:
    """
    params:
        N: int
            Size of this graph. This values is 0-index
        adj_list: List[List[int]]
            隣接リスト
    """
    def __init__(self, N: int):
        self.N = N
        self.adj_list = [[] for _ in range(N)]
    
    def add_edge(self, u: int, v: int, weight: float = 1):
        """u -> v の辺を追加する。"""
        self.adj_list[u].append((v, weight))
    
    def get_neighbors(self, u: int) -> List[Tuple[int, float]]:
        """頂点uから出る辺の隣接頂点と重みのリストを返す。"""
        return self.adj_list[u]

def dijkstra(graph: Graph, start: int) -> Dict[int, float]:
    """Dijkstraのアルゴリズムを用いて、指定された始点からグラフ内の全頂点への最短経路のコストを計算する。
    params:
        graph: Graph
            グラフ
        start: int
            始点
    return:
        List[float]
            始点から各頂点への最短経路のコストを含むリスト
    """
    N = graph.N
    distances = {v: float('inf') for v in range(N)}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# https://atcoder.jp/contests/abc340/tasks/abc340_d
if __name__=="__main__":
    N = int(input())
    G = Graph(N+1)
    for i in range(1, N):
        a, b, x = map(int, input().split())
        G.add_edge(i, i+1, a)
        G.add_edge(i, x, b)

    shortest_distances = dijkstra(G, 1)
    print(shortest_distances[N])