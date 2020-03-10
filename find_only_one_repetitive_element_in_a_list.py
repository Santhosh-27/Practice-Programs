'''
We are given an array arr[] of size n. Numbers are from 1 to (n-1) in random order. The array has only one repetitive element. We need to find the repetitive element.

Examples :

Input  : a[] = {1, 3, 2, 3, 4}
Output : 3

Input  : a[] = {1, 5, 1, 2, 3, 4}
Output : 1
'''
def find_only_one_repetitive(arr):
    result = arr[0]
    for i in range(1,len(arr)-1):
        result = result ^ arr[i]
    print(result)

if __name__ == '__main__':
    find_only_one_repetitive([1,3,2,3,4])