def solution(statues):
    if len(statues) == 1:
        return 0
    statues.sort()
    print(statues)
    if len(statues) == 2:
        return statues[1] - statues[0] - 1
    n = len(statues)
    r = 0
    for i in range(n - 1):
        d = statues[i + 1] - statues[i]
        if d > 1:
            r += d - 1
    return r


if __name__ == '__main__':
    print(solution([6, 2, 3, 8]))
