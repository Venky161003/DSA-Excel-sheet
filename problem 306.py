def isSafe(graph, v, colour, c, V):
    
    for i in range(V):

        if (graph[v][i] == 1 and colour[i] == c):
            return False

    return True


def graphColourUtil(graph, m, colour, v, V):

    if v == V:
        return True

    for c in range(1, m+1):

        if (isSafe(graph, v, colour, c, V) == True):

            colour[v] = c

            if (graphColourUtil(graph, m, colour, v+1, V) == True):

                return True

            colour[v] = 0

    return False

def graphColoring(graph, k, V):
    colour = [0] * V

    if (graphColourUtil(graph, k, colour, 0, V) == False):
        return False
    return True
