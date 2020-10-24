def bubble_sort(list):
    sorted_list = list[:]
    is_sorted = False
    while is_sorted == False:
        swaps = 0
        for i in range(len(list) - 1):
            if sorted_list[i] < sorted_list[i + 1]: # swap
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[i + 1]
                sorted_list[i + 1] = temp
                swaps += 1
                print(swaps)
        if swaps == 0:
            is_sorted = True
    return sorted_list

print(bubble_sort([99, 16, 4]))