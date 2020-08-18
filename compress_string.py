'''
Compress the string 
Input : AAABBCDDDD 
Output : 3A2BC4D
'''

from collections import OrderedDict


def compress(input):
    result_dict = OrderedDict()
    result_string = ''
    for char in input:
        if char.isalpha():
            if char not in result_dict.keys():
                result_dict[char] = 1
            else:
                result_dict[char] += 1

    for key in result_dict.keys():
        if result_dict[key] != 1:
            result_string += str(result_dict[key]) + key
        else:
            result_string += key

    print(result_string)


if __name__ == '__main__':
    input = 'AAABBCDDDD'
    compress(input)