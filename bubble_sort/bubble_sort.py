def bubble_sort(unsorted_list):
    # TODO: Implement bubble sort
    n= len(unsorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                # swap if the element found is greater than the next element
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

my_list= [64, 34, 25, 12, 22, 11, 90]
print("Unsorted list:", my_list)
bubble_sort(my_list)
print("Sorted list:", my_list)