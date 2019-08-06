# Code to parse the dictionary nested inside a list

L = [{"FixedName":"xyz","ImageUrl":"python:3"},
{"FixedName":"abc","ImageUrl":"go"},
{"FixedName":"utc","ImageUrl":"nginx"}]

for item in L:
    print(item['ImageUrl'])
    
