'''
You are given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array. Traverse array only once.
Input array   =  [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output array =  [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 
'''
def segregate0sand1s(arr):
    low = 0
    high = len(arr)-1
    while low < high:
        if arr[low] == 1:
            arr[low],arr[high] = arr[high],arr[low]
            high-=1
        else:
            low+=1
    print(arr)
    return 0

if __name__ == '__main__':
    arr = [0, 1, 0, 1, 1, 1] 
    result = segregate0sand1s(arr)