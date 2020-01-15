# Python3
# Given a string capitalize each word
# Example : hello world -> Hello World

def capitalize(s):
    s = str(s).split(" ")
    index = 0
    for word in s:
        s[index] = word.capitalize()
        index = index + 1
    s = " ".join(s)
    return s
    
if __name__ == '__main__':
    s = input()
    result = capitalize(s)
    print(result)
