from bisect import bisect_left, bisect_right

n, x = map(int,input().split())
array = list(map(int,input().split()))

print(bisect_right(array,x) - bisect_left(array,x))
