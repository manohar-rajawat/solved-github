def solutions(list_array):
    remove_count = 0
    while True:
        i = 0
        while i < (len(list_array) - 1):
            if list_array[i] == list_array[i+1]:
                list_array = list_array[:i]+list_array[i+2:]
                remove_count += 1
                break;
            i += 1
        else:
            break;
    return "Alice" if remove_count%2 == 1 else "Bob"
    
print (solutions([1,2,2,3,3,1,1]))
