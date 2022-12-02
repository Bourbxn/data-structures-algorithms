def counting_sort(arr: list) -> None:
    size = len(arr)
    output = [0] * size
    count = [0] * 10
    for i in range(0, size):
        count[arr[i]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
    for i in range(0, size):
        arr[i] = output[i]

def main():
    pass
    # arr = [4, 2, 2, 8, 3, 3, 1]
    # print(arr)
    # counting_sort(arr)
    # print(arr) 

if __name__ == '__main__':
    main()