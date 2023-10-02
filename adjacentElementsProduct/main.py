
def solution(inputArray):
    n = len(inputArray)
    if n == 2:
        return inputArray[0] * inputArray[1]
    r = min(inputArray)
    for i in range(n):
        if i < n - 1:
            p = inputArray[i] * inputArray[i + 1]
            if p > r:
                r = p
    return r


if __name__ == '__main__':
    print(solution([-23, 4, -3, 8, -12]))
