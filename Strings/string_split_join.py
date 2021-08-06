"""
String Split and Join
"""


def split_and_join(line):
    # write your code here

    # split string into a list
    split_line = line.split(" ")

    # join list items as one string, adding - separator between each
    new_string = "-".join(split_line)
    return new_string


if __name__ == '__main__':
    line = input('Enter a string: ')
    result = split_and_join(line)
    print(result)
# print(split_and_join('this is a string'))
