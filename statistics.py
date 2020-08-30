'''The code below calculates the mean'''
def my_mean(lst):
    total = sum(lst) #function that finds the sum of elements in the list
    n = len(lst) #function that finds the total number of elements in the list
    result = total/n #the mean gotten by dividing total by n 
    return result
    
'''The code below calculates the median'''
def my_median(lst):
    lst.sort() #sort the list so that it is ordinal(smallest to largest)
    n = len(lst) #get the total number of items in the list
    med1 = lst[n//2] #assign the position of the middle number to a variable
    med2 = lst[n//2 - 1] #assign the position of the number before the middle number to a variable
    if n % 2 == 0: #check if the number of items is even and if so, add the two midpoints and divide by two
        result = (med1 + med2)/2
    else:   #if the number of items is odd, compute just the midpoint
        result = med1
    return result
    
'''The code below calculates the mode'''
def my_mode(lst):
    count = 1 #initial value
    n = len(lst) #the total number of items in the list
    lst2 = [] #new list initiated to append recurring numbers
    new = 0 #counter to count the number of elements that repeat
    for i in range(n - 1): #a loop to check for every item in the range below the total number 
        if lst[i] == lst[i +1]: #if an item is equal to the next item, count it and add it to the new list
            new = lst.count(i)
            lst2.append(lst[i])
        elif lst[i] == lst[i - 1]: #if an item is equal to the item before it 
            new = lst.count(i) #count it and add it to the new list
            lst2.append(lst[i])
        if count <= new: #if the initial value is less than the count of items that are the same,
            count = new #reassingn the value of count
    return lst2[0]

'''The code below calculates the range'''
 def my_range(lst):
    max_num = max(lst) #function that finds the largest number in a list
    min_num = min(lst) #function that finds the smallest number in a list
    result = max_num - min_num #range is given by the differece
    return result 

'''The code below calculates the standard deviation'''
def my_stdev(lst):
    n = len(lst) #the total number of items in the list
    mean = my_mean(lst) #use the mean function defined to compute mean of the list
    lst2 = [] #initiate another list
    for i in lst: #for every item in the initital list, get the difference between the item and mean
                  #and square the result
        x = (i - mean)**2
        lst2.append(x) #append the values of the the result to a list
    lst3 = sum(lst2) #assign to a new variable, the sum of the items in this new list 
    result = (lst3/n)**0.5 #divide the total by the number of items and get the square root
    return result
