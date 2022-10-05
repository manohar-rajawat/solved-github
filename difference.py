def get_difference(list_array):
    Count = 0
    for ind,num in enumerate(list_array):
        if num <= 100 and num >= -100:
            if ind%2 == 0:
                Count += num
            else:
                Count -= num
    return Count
