def minimumAbsoluteDifference(arr):
    n = len(arr)

    diffs = [abs(arr[i] - arr[j]) for i in range(n-1) for j in range(i+1, n)]

    return min(diffs)


if __name__ == '__main__':
    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    result = minimumAbsoluteDifference(arr)

    print(str(result) + '\n')
