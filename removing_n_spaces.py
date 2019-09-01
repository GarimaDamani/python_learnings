# Code to remove n spaces from input string
from datetime import datetime


class RemoveSpaces:
    def __init__(self, string):
        self.string = string
        self.final_string = ''
        self.one_space = False

    def remove_n_spaces(self):
        for char in self.string:
            if char != ' ':
                self.one_space = False
                self.final_string += char
            elif self.one_space is not True:
                self.one_space = True
                self.final_string += char
            else:
                continue
        return self.final_string


if __name__ == '__main__':
    print(f'Please enter a string :')
    initial_string = str(input())
    start_time = datetime.now()
    remove_spaces = RemoveSpaces(initial_string)
    final_string = remove_spaces.remove_n_spaces()
    print(f'\nFinal string is :\n{final_string}')
    print(f'\nProcessed in time : {datetime.now() - start_time}')
