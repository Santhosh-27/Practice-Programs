'''
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.
Input :  {-2, -3, 4, -1, -2, 1, 5, -3}
Output : 7 that formed from [4,-1,-2,1,5]
'''
def longestsum(arr):
    current_max = arr[0]
    total_max = arr[0]
    starting_index = 0
    ending_index = 0
    for i in range(1,len(arr)):
        if (arr[i] >= current_max + arr[i]):
            starting_index = i
            current_max = arr[i]
        else:
            current_max = current_max+arr[i]
        # current_max = max(arr[i],current_max+arr[i])
        # total_max = max(current_max,total_max)
        if(current_max >= total_max):
            ending_index = i
            total_max = current_max
    print(starting_index,ending_index)
    return total_max,starting_index,ending_index
if __name__ == '__main__':
    arr = [-2,-3,4,-1,-2,1,5,-3]
    result,st_i,en_i = longestsum(arr)
    print("Maximum sum:{}".format(result))
    print("Subarray:{}".format(arr[st_i:en_i+1]))