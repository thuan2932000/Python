# Cau 7: Returns the number of values that appear two or more times
def count_duplicates(dictionary):
    duplicates = 0
    values = list(dictionary.values())
    for item in values:      
        if values.count(item) >= 2:
            duplicates = duplicates + 1     
            num_occurrences = values.count(item)
            for i in range(num_occurrences):
                values.remove(item)

    return duplicates
count_duplicates({'A': 1, 'B': 2, 'C': 2, 'D': 1, 'E': 3})