# Python3
# Read a given string, change the character at a given index and then print the modified string.
# Input 
# abracadabra
# 5 k
# Output : abrackdabra

def mutate_string(string, position, character):
    return string[:position] + str(character) + string[position+1:]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
