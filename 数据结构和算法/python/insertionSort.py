# 插入算法及其实现

def insertionSort(array):
    i = 1
    while i < len(array):
        value = array[i]
        j = i - 1
        while j >= 0:
            if array[j] > value:
                array[j+1] = array[j]
            else:
                break
            j -= 1
        array[j+1] = value
        i += 1
    return array

if __name__ == "__main__":
    sortArray = insertionSort([1,5,3,7,6,-2,4,9,8,9])
    print (sortArray)