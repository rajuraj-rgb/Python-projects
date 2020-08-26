def reverse_and_swap_functions(string):
    string = string[::-1].swapcase()
    print(string)
if __name__ == "__main__":
    string = input()
    reverse_and_swap_functions(string)