def max_index(myList):
    for index,number in enumerate(myList):
        if number == max(myList):
            return index 
     
    
print(max_index( [40, 50, 10, 90, 100, 70]))