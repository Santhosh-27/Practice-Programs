'''
Given an array of n elements which contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.
Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
Output : output_list = [20, 30, -20, 60]
'''
def find_duplicates(arr):
    #import pdb;pdb.set_trace()
    for i in range(len(arr)):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            print(abs(arr[i]))
if __name__ == '__main__':
	find_duplicates([1, 5, 3, 1, 4, 5, 5])