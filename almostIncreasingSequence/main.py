def solution(sequence):
    n = len(sequence) - 1
    dp = [0] * n
    i = 0
    while i < n:
        if sequence[i] < sequence[i + 1]:
            dp[i] = 1
        else:
            if sequence[i] == sequence[i + 1]:
                dp[i] = 0
            else:
                if i - 1 >= 0:
                    if sequence[i - 1] >= sequence[i + 1]:
                        if i + 1 < n:
                            if sequence[i + 2] > sequence[i]:
                                dp[i + 1] = 0
                                dp[i - 1] = 1
                            else:
                                dp[i - 1] = 0
        i += 1
    if sum(dp) < n - 1: return False
    else: return True


if __name__ == '__main__':
    print(solution([3, 5, 67, 98, 3]), "True")
    print(solution([1, 1, 1, 2, 3]), "False")
    print(solution([1, 2, 3, 4, 3, 6]), "True")
    print(solution([1, 2, 3, 4, 5, 3, 5, 6]), "False")
    print(solution([1, 2, 1, 2]), "False")
    print(solution([1, 3, 2]), "True")
    print(solution([10, 1, 2, 3, 4, 5]), "True")
