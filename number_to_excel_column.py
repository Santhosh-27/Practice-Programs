'''
Given a number N. The task is to identify the Excel column name 

Example : 
1- > Column A
2 - > B
26 -> Z
27 -> AA
28 -> AB....
'''

import string
def excel_number_to_column_name(num):
	result = ''
	while num:
		mod = (num-1)%26
		temp = chr(mod+65)
		result += temp
		num = int(num/26)
	return result[::-1]


if __name__ == '__main__':
	num = int(input("Enter a number to see the excel column name:"))
	result = excel_number_to_column_name(num)
	print("Excel column name : {}".format(result))