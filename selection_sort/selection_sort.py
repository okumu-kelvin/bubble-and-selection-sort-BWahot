def selection_sort(arr):
    # TODO: Implement selection sort
    n=len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

my_list = [34, 4, 25, 12, 2, 1, 9]
print("Unsorted list:", my_list)
selection_sort(my_list)
print("Sorted list:", my_list)
