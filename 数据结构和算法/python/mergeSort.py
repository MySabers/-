# 归并排序的实现

def mergeSort(array, p, r):
    if p >= r:
        return
    q = (p + r) // 2
    mergeSort(array, p, q)
    mergeSort(array, q + 1, r)
    merge(array, p, q, r)

    
def merge(array, p, q, r):
    i, j = p, q + 1
    tmp = []
    while i <= q and j <= r:
        if array[i] <= array[j]:
            tmp.append(array[i])
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    
    start, end = i, q
    if j <= r:
        start, end = j, r

    while start <= end:
        tmp.append(array[start])
        start += 1
    
    i = 0
    for i in range(r - p + 1):
        array[p + i] = tmp[i]


if __name__ == "__main__":
    arr = [1, 3, 5, 2, 4, 6, 9, 7, -1]
    mergeSort(arr, 0, len(arr) - 1)
    print (arr)