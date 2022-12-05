def binary_search(arr: list, val: int) -> int:
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
    #arr = [1,2,3,4,5,6,7]
    #print(binary_search(arr, 5))

if __name__ == '__main__':
    main()