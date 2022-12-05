def bucket_sort(arr):
    bucket = []
    for i in range(len(arr)):
        bucket.append([])
    for j in arr:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

def main():
    pass
    # arr = [.42, .32, .33, .52, .37, .47, .51]
    # print(arr)
    # arr = bucket_sort(arr)
    # print(arr)

if __name__ == '__main__':
    main()