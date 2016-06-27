# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

input_list = [2, 3, 6, 8, 9, 10, 11, 12]

def get_every_second(input_list):
    if type(input_list) != list:
        raise ValueError('Excepted a list')

    every_second = []
    for item in range(0, len(input_list)):
        if (item + 1) % 2 == 0:
            every_second.append(input_list[item])
    return every_second

print(get_every_second(input_list))
