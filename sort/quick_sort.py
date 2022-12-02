def partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1
 
def quick_sort(arr: list, low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def main():
    pass
    # arr = [1, 7, 4, 1, 10, 9, -2]
	# print(arr)
	# quick_sort(arr, 0, len(arr)-1)
	# print(arr)

if __name__ == '__main__':
    main()