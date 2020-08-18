'''
Selecting the pivot element as first element and putting the pivot element as in sorted place such that all elements before pivot are less than pivot and after pivot are greater than pivot
then sorting the first and second half recursively
'''


def partition(array,start,end):
    pivot = array[start]
    low = start+1
    high = end
    
    while True:
        while low <= high and array[high] >= pivot:
            high -= 1
        while low<= high and array[low] <= pivot:
            low += 1
        
        if low <= high:
            array[low],array[high] = array[high],array[low]
        else:
            break
            
    
    array[start],array[high] = array[high],array[start]
    return high


def quicksort(array,low,high):
    if low<= high:
        pi = partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)
        
    


if __name__ == '__main__':
	array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
	quicksort(array,0,len(array)-1)
	print(array)