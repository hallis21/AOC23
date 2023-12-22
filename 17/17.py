import random
import multiprocessing
import time

squares = [[x for x in y.strip()] for y in open("17").readlines()]
w = len(squares[0])
h = len(squares)
squares = [int(x) for y in squares for x in y]
to_idx = lambda c: c[0] + c[1] * w
to_xy = lambda i: (i % w, i // w)
dirs = [(0, (1, 0)), (1, (0, 1)), (2, (-1, 0)), (3, (0, -1))]

absolute_max_score = 000


def run(seed):
    # flatend

    # 0 east, 1 south, 2 west, 3 north

    # (((step1), (step2) ...), in_row, last_dir, score)
    cur_paths = [((0, 0), 0, 0, 0)]

    # idx: (in_row, last_dir, score, path)
    best_scores = {}

    ## Example input
    # 2413432311323
    # 3215453535623
    # 3255245654254

    while len(cur_paths) > 0:
        new_paths = []
        print(len(cur_paths))

        for path, in_row, last_dir, score in cur_paths:
            x, y = path
            random.shuffle(dirs)
            for dir, (dx, dy) in dirs:
                new_coords = (x + dx, y + dy)
                if (
                    # to_idx(x + dx, y + dy) in path
                    dir == (last_dir + 2) % 4
                    or x + dx < 0
                    or x + dx >= w
                    or y + dy < 0
                    or y + dy >= h
                    or (dir == last_dir and in_row >= 3)
                ):
                    continue
                # Do not spawn a path if it is already worse than the best path
                # And the in_row is the same or lower
                best_score = best_scores.get(to_idx(new_coords), None)
                if (
                    best_score is not None
                    and best_score[2] < score + squares[to_idx(new_coords)]
                    and best_score[0] <= in_row
                ):
                    # if dir == best_score[1] and (
                    #     in_row < best_score[0] or score < best_score[2]
                    # ):
                    #     # We need to check the continuation of best_score if in_row is less than the cached cont_in_row

                    #     # Spawn a path
                    #     # set the cont_in_row and cont_score to the best_score
                    #     # Do not update the rest of the best_score
                    #     pass

                    continue

                # new_path = (x + dx, y + dy)
                new_in_row = in_row + 1 if dir == last_dir else 1
                new_score = score + squares[to_idx(new_coords)]
                if new_score >= absolute_max_score:
                    continue
                new_paths.append((new_coords, new_in_row, dir, new_score))

                best_scores[to_idx(new_coords)] = (
                    new_in_row,
                    dir,
                    new_score,
                )

        cur_paths = new_paths
    return best_scores.get(to_idx((w - 1, h - 1)), None)


start = time.time()
r = run(0)
print("Time to run 1 iteration: ", time.time() - start)

exit()

# exit()
# Run the test 100 times and get the best result'
def run_iteration(x):
    return run(x)


best_score = None
with multiprocessing.Pool() as pool:
    results = pool.map(run_iteration, range(1000))
    for score in results:
        if score is None:
            continue
        if best_score is None or score[2] < best_score[2]:
            best_score = score

print("Best path to bottom right corner:")
print(best_score)


# best_score = best_scores.get(to_idx(w - 1, h - 1), None)
# print("Best path to bottom right corner:")
# print(best_score)

# # Draw the board with best path as #
# for i in range(len(squares)):
#     if i in best_score[3]:
#         squares[i] = "#"
#     else:
#         squares[i] = "."

# for y in range(h):
#     # 2 digit numbers
#     print(str(y + 1).zfill(2), "".join([str(x) for x in squares[y * w : (y + 1) * w]]))
