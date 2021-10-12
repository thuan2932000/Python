# Cau 9: Return a new dictionary that contains only the key/value pairs that occur in both dict1 and dict2.
def dict_interest(dict1, dict2):
    intersection = {}
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            intersection[key] = value

    return intersection
dict_interest({'a': 1, 'b': 2, 'c': 3}, {'a': 1, 'b': 2, 'd': 2})