# python 3
# You are given a string and your task is to swap cases.
# In other words, convert all lowercase letters to uppercase letters and vice versa.
# Example : Pythonist 2 → pYTHONIST 2

def swap_case(s):
    index = 0
    for i in s:
        if str(i).islower():
            s = s[:index] + str(i).upper()
        else:
            s = s[:index] + str(i).lower()
        index = index + 1
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
