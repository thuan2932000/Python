def same_first_last(L : list ) -> bool:
  if len(L) >= 2 and L[0] == L[-1]:
    print(True)
  else:
    print(False)

same_first_last([3, 4, 2, 8, 3])
same_first_last(['apple', 'banana', 'pear'])
same_first_last([4.0, 4.5])