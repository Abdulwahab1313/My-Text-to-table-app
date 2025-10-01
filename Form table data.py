import pandas as pd 
col = int(input("Enter no of column: "))
dictionary = {}
def dic():
    name_c = input("Enter name of column: ")
    rows = int(input("Enter no of rows: "))
    
    list = []
    for no in range(rows):
        include = input("Enter word: ")
        increase = list.append(include)
    add = dictionary.update({name_c : list})
    return  add
for no in range(col):
    print(dic())
table = pd.DataFrame(dictionary)
table.to_csv("/storage/emulated/0/Download/my_newentery.csv")
print(table)
