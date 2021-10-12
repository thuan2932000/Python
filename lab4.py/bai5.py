# Cau 5:  Takes a single dictionary as an argument and returns the number of distinct values
def count_values(dictionary):
    return len(set(dictionary.values()))
count_values({'A': 1, 'B': 2, 'C': 2, 'D':3})