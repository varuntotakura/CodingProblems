import numpy as np

def timestamp(pair):
    return pair[0]

def per_func(win_arr):
    values = []
    for _, d in win_arr:
        values.append(d)
    return int(np.percentile(values, 50))

def sliding_window_median(pairs):
    pairs.sort(key=timestamp)
    result = []
    win_size = 3
    window = []
    for i in range(len(pairs)):
        window.append(pairs[i])
        if len(window) == win_size:
            per = per_func(window)
            result.append((i, per))
            window.pop(0)
        else:
            result.append((i, -1))
    return result
    # per_w = []
    # count = 0
    # for i in range(len(pairs)):
    #     per_w.append(per_func(pairs[i:i+win_size]))
    #     if len(per_w) >= win_size:
    #         result.append((i, per_w[i-count]))
    #     else:
    #         result.append((i, -1)) 
    #         count += 1
    # return result
    # for i in range(len(pairs)):
    #     timestamp = pairs[i][0]
    #     window = []
    #     for j in range(max(0, i-2), i+1):
    #         window.append(pairs[j][1])
    #     if len(window) == win_size:
    #         median = int(np.percentile(window, 50))
    #     else:
    #         median = -1
    #     result.append((timestamp, median))
    # return result

pairs = [(0, 60), (1, 70), (2, 80), (3, 90), (4, 40), (5, 30)]
print(sliding_window_median(pairs))