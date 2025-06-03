def pairwise_product(List1, List2):
    newList = []
    if len(List1) == len(List2):
        for index, number in enumerate(List1):
            newNumber = number * List2[index]
            newList.append(newNumber)
        return newList
    
print(pairwise_product([40, 50, 10, 90] , [6, 2, 2, 5]))
            