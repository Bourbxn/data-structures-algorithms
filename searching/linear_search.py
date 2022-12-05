def linear_search(arr: list, val: int) -> int:
    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1

def main():
    pass
    #arr = [1,2,3,4,5,6,7]
    #print(linear_search(arr,4))

if __name__ == '__main__':
    main()

