# 冒泡排序的实现, 从小到大，左边为无序，右边为有序
def bubbleSortFromSmallToLarge(array):   
    i = 0
    while i < len(array):
        flag = False
        j = 0
        while j < len(array) - i - 1:
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
                flag = True
            j += 1
        if not flag:
            break
        i += 1
    return array

#冒泡排序，从大到小，左边为有序，右边为无序
def bubbleSortFromLargeToSmall(array):
    i = 0
    while i < len(array):
        flag = False
        j = len(array) - 1
        while j > 0 + i:
            if array[j] > array[j-1]:
                array[j], array[j-1] = array[j-1],array[j]
                flag = True
            j -= 1
        if not flag:
            break
        i += 1
    return array

if __name__ == "__main__":
    arr = bubbleSortFromLargeToSmall([7, 6, 8, 9, 1, 4, 2, 6, 7])
    print(arr)
