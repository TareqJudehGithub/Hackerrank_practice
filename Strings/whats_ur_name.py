"""
What's Your Name?

"""
#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(*args):
    return f'Hello {args[0]} {args[1]}! You just delved into python.'


if __name__ == '__main__':
    first_name = input('First name: ').title()
    last_name = input('Last name: ').title()
    print(print_full_name(first_name, last_name))