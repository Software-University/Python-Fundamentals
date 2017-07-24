n = int(input())

continents = {}

for i in range(n):
    strs = input().split(" ")
    if strs[0] in continents:
        if strs[1] in continents[strs[0]]:
            continents[strs[0]][strs[1]].append(strs[2])
        else:
            continents[strs[0]][strs[1]] = [strs[2]]
    else:
        continents[strs[0]] = {
            strs[1]: [strs[2]]
        }
print(continents)
