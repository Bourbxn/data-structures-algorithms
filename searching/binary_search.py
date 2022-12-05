def binary_search(arr: list, val: int) -> int:
    arr = sorted(arr)
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if val == arr[mid]:
            return mid
        elif val > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def main():
    pass
    #arr = [5,2,1,4,7,6,3]
    #print(binary_search(arr, 6))

if __name__ == '__main__':
    main()