def smaller_indices(List1,List2):
    small_indices = []
    if len(List1) == len(List2):
        for index,number in enumerate(List1):
            if number < List2[index]:
                small_indices.append(index)
    return small_indices
                
print(smaller_indices( [40, 50, 10, 90, 100, 70], [60, 20, 19, 95, 30, 20] ))
            