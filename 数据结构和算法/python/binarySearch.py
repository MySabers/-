# 二分查找的实现

# 非递归的方式
def brinarySearch(data, searchData):
    high = len(data) - 1
    low = 0
    while high >= low:
        # middle = (high + low) // 2
        middle = low + ((high - low) >> 1)
        if searchData == data[middle]:
            return middle
        elif searchData > data[middle]:
            low = middle + 1
        else:
            high = middle - 1

# 递归的方式
def brinarySearch2(data, searchData, low, high):
    middle = low + ((high - low) >> 1)
    if low > high:
        return -1
    if searchData == data[middle]:
        return middle
    elif searchData > data[middle]:
        return brinarySearch2(data, searchData, middle + 1, high)
    else:
        return brinarySearch2(data, searchData, low, middle - 1)

# 查找第一个值等于给定值的数组下标
def brinarySearch3(data, searchData, low, high):
    middle = low + ((high - low) >> 1)
    if low > high:
        return -1
    if searchData == data[middle]:
        if middle == 0 or data[middle - 1] != searchData:
            return middle
        else:
            return brinarySearch3(data, searchData, low, middle - 1)
    elif searchData > data[middle]:
        return brinarySearch3(data, searchData, middle + 1, high)
    else:
        return brinarySearch3(data, searchData, low, middle - 1)

# 查找最后一个值等于给定值的数组下标
def brinarySearch4(data, searchData, low, high):
    middle = low + ((high - low) >> 1)
    if low > high:
        return -1
    if searchData == data[middle]:
        if middle == len(data) or data[middle + 1] != searchData:
            return middle
        else:
            return brinarySearch4(data, searchData, middle + 1, high)
    elif searchData > data[middle]:
        return brinarySearch4(data, searchData, middle + 1, high)
    else:
        return brinarySearch4(data, searchData, low, middle - 1)

# 查找第一个大于等于给定值的元素
def brinarySearch5(data, searchData, low, high):
    middle = low + ((high - low) >> 1)
    if low > high:
        return -1
    elif data[middle] >= searchData:
        if middle == 0 or data[middle - 1] < searchData:
            return middle
        else:
            return brinarySearch5(data, searchData, low, middle - 1)
    else:
        return brinarySearch5(data, searchData, middle + 1, high)

# 查找最后一个小于等于给定值的元素
def brinarySearch6(data, searchData, low, high):
    middle = low + ((high - low) >> 1)
    if low > high:
        return -1
    elif data[middle] >= searchData:
        if middle == 0 or data[middle - 1] < searchData:
            return middle - 1
        else:
            return brinarySearch6(data, searchData, low, middle - 1)
    else:
        return brinarySearch6(data, searchData, middle + 1, high)

if __name__ == "__main__":
    mydata = [1,3,15, 88, 88, 88,100]
    index = brinarySearch(mydata, 67)
    index2 = brinarySearch2(mydata, 67, 0, len(mydata) - 1)
    index3 = brinarySearch3(mydata, 88, 0, len(mydata) - 1)
    index4 = brinarySearch4(mydata, 88, 0, len(mydata) - 1)
    index5 = brinarySearch5(mydata, 14, 0, len(mydata) - 1)
    index6 = brinarySearch6(mydata, 88, 0, len(mydata) - 1)
    print (index6)