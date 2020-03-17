'''
Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.
'''
def longestsum(arr):
    current_sum = 0
    starting_index = 0
    n = len(arr)
    k = 3
    for i in range(0,(n-k)+1):
        if sum(arr[i:i+k]) > current_sum:
            starting_index = i
            current_sum = sum(arr[i:i+k])
        # current_sum = max(current_sum,sum(arr[i:i+k]))
    return current_sum,starting_index

if __name__ == '__main__':
    arr = [5,2,-1,0,3,7]
result,st_i = longestsum(arr)
print(result)
print(arr[st_i:st_i+3])