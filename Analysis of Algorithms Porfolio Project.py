# Alejandro Grau
# CS 325 Project
# 5/24/2022

import heapq, copy


def solve_puzzle(board, source, destination):
    """
    solve_puzzle takes a 2D board with barriers in certain cells,
    and determines the shortest path to get from source to destination

    board: 2D matrix puzzle. Cells will be marked '-' if empty, '#' if barrier
    source: tuple representing coordinates of starting cell
    destination: tuple representing coordinates of destination cell
    return: A tuple
            [0]: A list of tuples representing the indices of the shortest path from source to destination
            [1]: A string with directions taken to get from source to destination (ex. 'DDRULUUDRRRDL')
    """
    # Initialize variables, matrices
    m, n = len(board), len(board[0])
    directions = [('D', (1, 0)), ('R', (0, 1)), ('U', (-1, 0)), ('L', (0, -1))]

    visited = [[False for x in range(n)] for y in range(m)]
    # Shortest path will contain the list of coordinates taken to node
    shortest_path = [[[] for x in range(n)] for y in range(m)]

    # path_string will contain the directions taken to get to node
    path_string = [['' for x in range(n)] for y in range(m)]

    # Initialize for source
    visited[source[0]][source[1]] = True
    shortest_path[source[0]][source[1]].append((source[0], source[1]))


    # Initialize priority queue
    priority_queue = []
    # Append tuples in the form (weight, (x, y))
    heapq.heappush(priority_queue, (0, (source[0], source[1])))

    # Breadth First Search
    while len(priority_queue) > 0:
        curr_weight, curr_coords = heapq.heappop(priority_queue)

        # End case: if we reached destination, return path to get there
        #    Final index in list will be string of directions
        if curr_coords == destination:
            return shortest_path[curr_coords[0]][curr_coords[1]], path_string[curr_coords[0]][curr_coords[1]]

        # For each direction away from current node, If it goes to an empty unvisited node, process it
        for direction, direction_difference in directions:
            x = curr_coords[0] + direction_difference[0]
            y = curr_coords[1] + direction_difference[1]

            if x < 0 or y < 0 or x >= m or y >= n:
                continue  # Out of bounds
            if board[x][y] == '#':
                continue  # Barrier
            if visited[x][y]:
                continue  # Already visited

            # Shortest path to next node is from current node
            shortest_path[x][y] = copy.deepcopy(shortest_path[curr_coords[0]][curr_coords[1]])
            path_string[x][y] = copy.deepcopy(path_string[curr_coords[0]][curr_coords[1]])
            # Add next node to path
            shortest_path[x][y].append((x, y))
            path_string[x][y] += direction

            visited[x][y] = True

            # Push next node to heap
            heapq.heappush(priority_queue, (curr_weight + 1, (x, y)))

    # While loop terminated and we haven't reached destination, puzzle is insolvable
    return None


if __name__ == '__main__':
    puzzle = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '-', '-'],
        ['#', '-', '#', '#', '-']
    ]
    print(solve_puzzle(puzzle, (0, 0), (3, 4)))
