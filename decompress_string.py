'''
Decompress the string 
Input : 3A2BC4D
Output : AAABBCDDDD
'''
def decompress(input):
	result_string = ''
	number = ''
	for char in input:
		if char.isnumeric():
			number += char
		elif char.isalpha():
			if number:
				new = int(number)*char
				result_string += new
				number = ''
			else:
				result_string += char
				
	print(result_string)





if __name__ == '__main__':
	input = '10A2BC4D'
	decompress(input)