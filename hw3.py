def quick_sort(arr):
    # 數組長度小於等於1，直接返回該數組
    if len(arr) <= 1:
        return arr

    # 選擇基準點
    pivot = arr[0]

    # 構建左子數組
    left = [x for x in arr[1:] if x <= pivot]

    # 構建右子數組
    right = [x for x in arr[1:] if x > pivot]

    # 左子數組和右子數組進行快速排序，並合併結果
    return quick_sort(left) + [pivot] + quick_sort(right)


# 測試
unsorted_array = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
sorted_array = quick_sort(unsorted_array)
print(sorted_array)
