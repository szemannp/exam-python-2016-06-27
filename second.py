# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def write_str_to_file(filename, input_str):
    try:
        with open(filename, 'a') as file_to_write:
            new_str = input_str + input_str + input_str
            file_to_write.write(new_str)
        file_to_write.close()
    except IOError:
        pass

write_str_to_file('ize.txt', 'valami')
