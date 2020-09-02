def my_mean(lst):
    """Function to compute the mean of of a list
    
    Args:
        list
    
    Returns:
        float: the mean of the list
    """
    
    total = sum(lst)  #finds the sum of elements in the list
    n = len(lst)      #finds the total number of elements in the list
    result = total/n  #the mean gotten by dividing total by n 
    return result

def my_median(lst):
    """Function that computes the median of a given list
    
    Args:
        list
        
    Returns:
        float: median of list
    """
    
    lst.sort()           #sort the list so that it is ordinal(smallest to largest)
    n = len(lst)         #get the total number of items in the list
    med1 = lst[n//2]     #assign the position of the middle number to a variable
    med2 = lst[n//2 - 1] #assign the position of the number before the middle number to a variable
    if n % 2 == 0:       #check if the number of items is even and if so, add the two midpoints and divide by two
        result = (med1 + med2)/2
    else:               #if the number of items is odd, compute just the midpoint
        result = med1
    return result


def my_range(lst):
    """Function that calculates the range of a list that is max - min
    
    Args: 
        list
        
    Returns:
        float: range of the list
    """
    
    max_num = max(lst) #function that finds the largest number in a list
    min_num = min(lst) #function that finds the smallest number in a list
    result = max_num - min_num #range is given by the differece
    return result

def my_stdev(lst):
    """Function that computes the standard deviation (spread from the mean) of a list
    
    Args:
        list
    
    Returns:
        float: standard deviation of the list
    """
    
    n = len(lst)        #the total number of items in the list
    mean = my_mean(lst) #use the mean function defined to compute mean of the list
    lst2 = []           #initiate another list
    for i in lst:       #for every item in the initital list, get the difference between the item and mean
                        #and square the result
        x = (i - mean)**2
        lst2.append(x)  #append the values of the the result to a list
    lst3 = sum(lst2)    #assign to a new variable, the sum of the items in this new list 
    result = (lst3/n)**0.5 #divide the total by the number of items and get the square root
    return result


def my_stats(data):
    """Function that computes the summary statistics of a given dataset based on the previously defined functions
    
    Args: 
        dataset
    
    Returns:
        float: length of dataset
        float: mean of data
        float: standard deviation of data
        float: median of data
        float: range of data
    """
    print('Count =', len(data))
    print('Mean =', my_mean(data))
    print('Standard deviation =', my_stdev(data))
    print('Median =', my_median(data))
    print('Range =', my_range(data))
