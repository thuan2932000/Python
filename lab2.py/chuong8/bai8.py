def is_longer(L1: list, L2: list) -> bool:
  if len(L1) > len(L2):
    print(True)
  else:
    print(False)
is_longer([1, 2, 3], [4, 5])
is_longer(['abcdef'], ['ab', 'cd', 'ef'])
is_longer(['a', 'b', 'c'], [1, 2, 3])