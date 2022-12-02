def selection_sort(arr: list) -> None:
    n = len(arr)
    for step in range(n):
        min_idx = step
        for i in range(step + 1, n):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[step], arr[min_idx]) = (arr[min_idx], arr[step])

def main():
    pass
    # arr = [-2, 45, 0, 11, -9]
	# print(arr)
	# selection_sort(arr)
	# print(arr)

if __name__ == '__main__':
    main()