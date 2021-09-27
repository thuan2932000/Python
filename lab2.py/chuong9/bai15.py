width = 1
while width < 8:
 print('T' * width)
 width += 1
width = 1
while width < 8:
 print(' ' * (7 - width), 'T' * width, sep='')
 width += 1