from collections import defaultdict
import heapq


def dijkstra(inp, mi=1, mx=3):
    h, w = len(inp), len(inp[0])
    i = 0

    # Start top left, add the two possible moves to the heap
    # The heap keeps track of moves, not positions
    # cost, (x,y (dx, dy))
    heap = [(0, (0, 0, 1, 0)), (0, (0, 0, 0, 1))]

    dists = defaultdict(lambda: float("inf"))

    while heap:
        cost, (x, y, dx, dy) = heapq.heappop(heap)

        # If we reached the bottom right, we're done
        if x == w - 1 and y == h - 1:
            return cost



        if cost > dists[(x, y, dx, dy)]:
            continue
    


        # find the possible new moves
        possible_moves = (-dy, dx), (dy, -dx)
        for mox, moy in possible_moves:
            new_cost = cost
            for distance in range(1, mx + 1):
                # new position
                nx = x + mox * distance
                ny = y + moy * distance

                # Check bounds
                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue

                new_cost += inp[ny][nx]

                if distance < mi:
                    continue

                # print(nx, ny, new_cost)
                # Add the new moves to the heap

                # for each square check the two possible moves

                if new_cost < dists[(nx, ny, mox, moy)]:
                    dists[(nx, ny, mox, moy)] = new_cost
                    heapq.heappush(heap, (new_cost, (nx, ny, mox, moy)))
                # print(
                #     (
                #         (nx, ny, mox, moy),
                #         new_cost,
                #     )
                # )


    return -1


# Example grid
squares = [[int(x) for x in y.strip()] for y in open("17").readlines()]

result = dijkstra(squares, 4, 10)


print("Lowest cost path:", result)
