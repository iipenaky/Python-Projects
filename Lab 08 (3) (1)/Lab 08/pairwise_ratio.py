def pairwise_ratio(List1, List2):
    newList = []
    if len(List1) == len(List2):
        for index, number in enumerate(List1):
            newNumber = number / List2[index]
            newList.append(newNumber)
        return newList
    
print(pairwise_ratio([40, 50, 10, 90], [60, 20, 19, 95]))