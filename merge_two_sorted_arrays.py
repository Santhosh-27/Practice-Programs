'''
Given two sorted arrays, the task is to merge them in a sorted manner.

Examples:

Input: arr1[] = { 1, 3, 4, 5}, arr2[] = {2, 4, 6, 8}
Output: arr3[] = {1, 2, 3, 4, 4, 5, 6, 8}

Input: arr1[] = { 5, 8, 9}, arr2[] = {4, 7, 8}
Output: arr3[] = {4, 5, 7, 8, 8, 9}
'''
def merge_array(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    i,j = 0,0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i = i+1
        elif arr1[i] > arr2[j]:
            print(arr2[j])
            j = j+1
        elif arr1[i] == arr2[j]:
            print(arr1[i])
            i = i+1
            j = j+1
    while i < m:
        print(arr1[i])
        i = i+1
    while j<n:
        print(arr2[j])
        j = j+1
            

if __name__ == '__main__':
    arr1 = [1, 3, 4, 5]
    arr2 = [2, 4, 6, 8]
    result = merge_array(arr1,arr2)