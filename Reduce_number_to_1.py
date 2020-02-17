'''
Given a number N. The task is to reduce the given number N to 1 in the minimum number of steps. You can perform any one of the below operations in each step.

Operation 1: If the number is even then you can divide the number by 2.
Operation 2: If the number is odd then you are allowed to perform either (n+1) or (n-1).
You need to print the minimum number of steps required to reduce the number N to 1 by performing the above operations.
'''


def countsteps(n):
    if n==1:
        return 0
    elif n%2 == 0:
        return 1 + countsteps(n/2)
    else:
        return 1 + min(countsteps(n-1),countsteps(n+1))





if __name__ == '__main__':
    f = int(input("Enter the number:"))
    result = countsteps(f)
    print(result)