def bubble_sort(arr: list) -> None:
    n, swapped = len(arr), False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break

def main():
    pass
    # arr = [64, 34, 25, 12, 22, 11, 90]
    # print(arr)
    # bubble_sort(arr)
    # print(arr) 

if __name__ == '__main__':
    main()

