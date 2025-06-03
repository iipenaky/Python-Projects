def min_index(myList):
    for index,number in enumerate(myList):
        if number == min(myList):
            return index 
     
    
print(min_max( [40, 50, 10, 90, 100, 70]))