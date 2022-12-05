def jump_search(arr: list , val: int) -> int:
    n = len(arr)
    step = n**(1/2)
    prev = 0
    while arr[int(min(step, n)-1)] < val:
        prev = step
        step += n**(1/2)
        if prev >= n:
            return -1
    while arr[int(prev)] < val:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == val:
        return int(prev)
    return -1

def main():
    pass
    #arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]
    #print(jump_search(arr, 55))

if __name__ == '__main__':
    main()
 
 