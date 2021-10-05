elements = []

with open('D:/alkaline_metals.txt', 'r') as source:
    for line in source:
        elements.append(line.strip().split())

print(elements)