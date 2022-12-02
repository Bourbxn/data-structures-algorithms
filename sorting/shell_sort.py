def shell_sort(arr: list) -> None:
    interval, n = len(arr) // 2, len(arr)
    while interval > 0:
        for i in range(interval, n):
            temp = arr[i]
            j = i
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        interval //= 2

def main():
    pass
    # arr = [ 12, 34, 54, 2, 3]
    # print(arr)
    # shell_sort(arr)
    # print(arr)

if __name__ == '__main__':
    main()