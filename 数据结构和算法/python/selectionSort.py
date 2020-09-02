# 选择排序的实现
def selectionSort(array):
    i = 0
    while i < len(array):
        j = i
        minNum = array[j]
        minNumIndex = j
        while j < len(array):
            if minNum > array[j]:
                minNum = array[j]
                minNumIndex = j
            j += 1
        array[minNumIndex] = array[i]
        array[i] = minNum
        i += 1
    return array

if __name__ == "__main__":
    arr = selectionSort([7,2,34,9,-1,7])
    print (arr)