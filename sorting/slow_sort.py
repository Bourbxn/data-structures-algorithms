def slow_sort(arr, i, j):
	if (i >= j):
		return
	m = (i + j) // 2
	slow_sort(arr, i, m)
	slow_sort(arr, m + 1, j)
	if (arr[j] < arr[m]):
		temp = arr[m]
		arr[m] = arr[j]
		arr[j] = temp
	slow_sort(arr, i, j - 1)

def main():
    pass
    # arr = [6, 8, 9, 4, 12, 1]
    # slow_sort(arr, 0, len(arr)-1)
    # print(arr)

if __name__ == '__main__':
    main()