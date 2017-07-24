contests = {}
contests["Basics"] = {
    'task1': "Lesna zadachka",
    'task2': "Trudna zadachka"
}

for name in contests:
    print(name)
    for task in contests[name]:
        print ("\t", task)
    print()

print(len(contests))