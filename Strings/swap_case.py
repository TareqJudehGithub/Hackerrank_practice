"""
sWAP cASE
"""

def swap_case(string):

    swapped_string = str()

    for char in string:
        if char == char.lower():
            swapped_string += char.upper()
        else:
            swapped_string += char.lower()

    return swapped_string


print(swap_case('10AaAa_BbBb9'))

