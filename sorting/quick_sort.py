def quick_sort(numbers_list):
    n = len(numbers_list)
    if n <= 1:
        return numbers_list

    pivot = numbers_list.pop()
    lesser_list = []
    greater_list = []

    for number in numbers_list:
        if number <= pivot:
            lesser_list.append(number)
        else:
            greater_list.append(number)
    
    return quick_sort(lesser_list) + [pivot] + quick_sort(greater_list)


if __name__ == "__main__":
    print(quick_sort([2,12,8,43,2,1,3,6,8,9,23]))
    print(quick_sort([9,2,3,1,4,5,7,4,2,1,34,67,8,765,123,2,1]))
