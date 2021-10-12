# Cau 1:  takes a list of integers as its input argument. Let returns a set of those integers occurring two or more times in the list
def find_dups(L):
    """ (list) -> set
    Return the number of duplicates numbers from L.
    >>> find_dups([1, 1, 2, 3, 4, 2, 2])
    {1, 2}
    >>> find_dups([1, 2, 3, 4])
    set()
    """
    elem_set = set()
    dups_set = set()
    for entry in L:
        len_initial = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)
list_integers = [1,1,2,2,3,3,4,5,6,7,8,9]
find_dups(list_integers)