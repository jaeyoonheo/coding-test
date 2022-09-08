def cutting(array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    sum = 0
    for item in array:
        if item > mid:
            sum += (item - mid)
    if sum < target:
        return cutting(array, start, mid - 1, target)
    else:
        if cutting(array, mid + 1, end, target) == -1:
            return mid
        else:
            return cutting(array, mid + 1, end, target)


n, m = map(int, input().split())
ricecake = list(map(int, input().split()))
end = max(ricecake)

print(cutting(ricecake, 0, end, m))
