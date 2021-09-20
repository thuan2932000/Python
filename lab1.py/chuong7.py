#bai1
print('hello'.upper())
print('Happy Birthday!'.lower())
print('WeeeEEEEeeeEEEEeee'.swapcase())
print('ABC123'.isupper())
print( 'aeiouAEIOU'.count('a'))
print('hello'.endswith('o'))
print('hello'.startswith('H'))
print('Hello {0}'.format('Python'))
print('Hello {0}! Hello {1}!'.format('Python', 'World'))

#bai2
a = 'tomato'
print('Tổng chữ o trong câu là: ',a.count('o'))
#bai3 
b = 'tomato'
for o in b:
    b.index('o' + str('1'))
print(b)
