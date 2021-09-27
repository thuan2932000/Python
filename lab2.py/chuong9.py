#bai1
celegans_phenotypes = ['Emb','Him', 'Unc', 'Lon', 'Dpy', 'Sma']
for phenotype in celegans_phenotypes:
 print(phenotype)

#bai2
half_lives = [87.74, 24110.0,6537.0, 14.4, 376000.0]
for value in half_lives:
 print(value, end=' ')

#bai3
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
for count in whales:
 more_whales.append(count + 1)
print(more_whales)

#bai4
#a.
alkaline_earth_metals = [[4, 9.012], [12, 24.305],[20, 40.078], [38, 87.62],[56, 137.327], [88, 226]]
#b.
for inner_list in alkaline_earth_metals:
 print("inner_list[0]",inner_list[0])
 print("inner_list[1]",inner_list[1])
#c.
number_and_weight = []
for inner_list in alkaline_earth_metals:
 number_and_weight.append(inner_list[0])
 number_and_weight.append(inner_list[1])
 print(number_and_weight[0])
 print(number_and_weight[1])

#bai6
text = ""
while text.lower() != "quit":
 text = input("Please enter 'QUIT' or 'quit' to exit: ")
 if text == "quit":
  print("…exiting program")
 elif text =="QUIT":
   print("…exiting program")
 else:
  print("Unknown compound")

#bai7
country_populations = [1295, 23, 7, 3, 47, 21]
total = 0
for population in country_populations:
 total += population
print(total)


#bai9
for number in range(33, 50):
 print(number)

 #bai10
 for number in range(10):
  print(10 - number, end=' ')

#bai11
sum = 0
count = 0
for number in range(2,23):
 sum += number
 count += 1
average = sum / count
print(average)

#bai12
def remove_neg(num_list):
 index = 0
 while index < len(num_list):
  if num_list[index] < 0:
    del num_list[index]
  else:
    index += 1

#bai13
for width in range(1, 8):
 print('T' * width)

#bai14
for width in range(1, 8):
 print(' ' * (7 - width), 'T' * width, sep='')

#bai15
width = 1
while width < 8:
 print('T' * width)
 width += 1
width = 1
while width < 8:
 print(' ' * (7 - width), 'T' * width, sep='')
 width += 1



