phonebook = []
phonebook.append(123)
#phonebook += "1234"
#phonebook.extend("1234")
phonebook.append([1,2,3,4])
phonebook.extend([1,2,3,4])
phonebook += ([1,2,3,4])
for x in phonebook:
    print(x)