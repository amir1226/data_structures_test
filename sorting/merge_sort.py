''' RETURN A NEW ARRAY
def merge_two_sorted_list(list_a, list_b):
    sorted_list = []
    len_a = len(list_a)
    len_b = len(list_b)

    i=j=0
    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            sorted_list.append(list_a[i])
            i += 1
        else:
            sorted_list.append(list_b[j])
            j += 1

    if i == len_a:
        sorted_list += list_b[j:]
    else:
        sorted_list += list_a[i:]

    return sorted_list


def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left, right)
'''

def merge_two_sorted_list(list_a, list_b, arr):
    len_a = len(list_a)
    len_b = len(list_b)

    i=j=k=0

    while i < len_a and j < len_b:
        if list_a[i] <= list_b[j]:
            arr[k] = list_a[i]
            i += 1
        else:
            arr[k] = list_b[i]
            j += 1
        k += 1

    if i == len_a:
        arr[k:] = list_b[j:]
    else:
        arr[k:] = list_a[i:]

def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_list(left, right, arr)

if __name__ == "__main__":
    # a = [5,8,12,34]
    # b = [7,9,23,31]

    # print(merge_two_sorted_list(a,b))
    arr = [2,1,2,34,56,12,123,412,2,1,25]
    merge_sort(arr)
    print(arr)

    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)