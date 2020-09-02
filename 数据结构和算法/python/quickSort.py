# 快速排序的实现

def quickSort(array, q, r):
    if (q >= r):
        return 
    p = partition(array, q, r)
    quickSort(array, q, p - 1)
    quickSort(array, p + 1, r)

def partition(array, q, r):
    x, y = q, q
    while x < r:
        if (array[x] <= array[r]):
            array[x], array[y] = array[y], array[x]
            y += 1
        x += 1
    array[x], array[y] = array[y], array[x]
    return y


if __name__ == "__main__":
    array = [1,5,3,6,-1,22,6, -2, 11]
    quickSort(array, 0, len(array) - 1)
    print (array)