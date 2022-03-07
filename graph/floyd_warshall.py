INF = 9999

def print_solution(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if (distance[i][j] == INF):
                print("INF", end = " ")
            else:
                print(distance[i][j], end = " ")
        print(" ")

def floyd_marshall(nv, graph):
    distance = graph

    for vertice in range(nv):
        for i in range(nv):
            for j in range(nv):
                distance[i][j] = min(distance[i][j], distance[i][vertice] + distance[vertice][j])

    print_solution(nv, distance)

if __name__ == "__main__":
    g = [
            [0, 8, INF, 1],
            [INF, 0, 1, INF],
            [4, INF, 0, INF],
            [INF, 2, 9, 1]
        ]
    
    floyd_marshall(4, g)
