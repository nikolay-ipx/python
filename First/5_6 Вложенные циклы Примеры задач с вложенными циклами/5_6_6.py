arr = list(map(int, input().split()))
for i in range(len(arr)):
	min_v = arr[i]
	k = i
	for j in range(i, len(arr)):
		if arr[j] < min_v:
			min_v = arr[j]
			k = j
	arr[i], arr[k] = arr[k], arr[i]
print(*arr)
