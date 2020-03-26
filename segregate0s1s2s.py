'''
Segregate 0s , 1s and 2s in an array
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
'''
def segregate0s1s2s(arr):
    low = 0
    high = len(arr)-1
    mid = 0
    while(mid<=high):
        if arr[mid] == 0:
            arr[low],arr[mid]=arr[mid],arr[low]
            low+=1
            mid+=1
        elif arr[mid] == 1:
            mid = mid+1
        else:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    print(arr)


if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 
    result = segregate0s1s2s(arr)