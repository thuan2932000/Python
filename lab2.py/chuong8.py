#bai1
kingdoms =['Bacteria', 'Protozoa', 'Chromista','Plantae', 'Fungi','Animalia']
#câu a
print(kingdoms[0])
#câu b
print(kingdoms[5])
#câu c
print(kingdoms[:3])
#câu d
print(kingdoms[2:5])
#câu e
print(kingdoms[4:])
#câu f
print(kingdoms[1:0])

#bai2
kingdoms =['Bacteria', 'Protozoa', 'Chromista','Plantae', 'Fungi','Animalia']
#câu a
print(kingdoms[-6])
#câu b
print(kingdoms[-1])
#câu c
print(kingdoms[-6:-3])
#câu d
print(kingdoms[-4:-1])
#câu e
print(kingdoms[-2:])
#câu f
print(kingdoms[-1:-2])

#bai3
appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
appointments.append('16:30')
appointments

#bai4
ids =[4353, 2314, 2956, 3382, 9362, 3900]
#cau a. 
ids.remove(3382)
print(ids)
#cau b. 
ids.index(9362)
print(ids)
#cau c. 
ids.insert(ids.index(9362) + 1, 4499)
print(ids)
#cau d. 
ids = ids + [5566, 1830]
print(ids)
#cau e. 
ids.reverse()
print(ids)
#cau f. 
ids.sort()
print(ids)

#bai5
alkaline_earth_metals = ['metals—beryllium','magnesium', ' calcium',' strontium','barium','radium']
#Cau a. 
alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
#Cau b. 
print(alkaline_earth_metals[5], alkaline_earth_metals[-1])
#Cau c. 
print(len(alkaline_earth_metals))
#Cau d. 
print(max(alkaline_earth_metals))

#bai6
#Cau a. 
temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
print(temps)
#Cau b. 
temps.sort()
print(temps)
#Cau c.
cool_temps = temps[0:2]
print(cool_temps)
warm_temps = temps[2:]
print(warm_temps)
#Cau d. 
temps_in_celsius = cool_temps + warm_temps
print(temps_in_celsius)

#bai7
def same_first_last(L : list ) -> bool:
  if len(L) >= 2 and L[0] == L[-1]:
    print(True)
  else:
    print(False)

same_first_last([3, 4, 2, 8, 3])
same_first_last(['apple', 'banana', 'pear'])
same_first_last([4.0, 4.5])

#bai8 
def is_longer(L1: list, L2: list) -> bool:
  if len(L1) > len(L2):
    print(True)
  else:
    print(False)
is_longer([1, 2, 3], [4, 5])
is_longer(['abcdef'], ['ab', 'cd', 'ef'])
is_longer(['a', 'b', 'c'], [1, 2, 3])

#bai9
values = [0, 1, 2]
values[1] = values

#bai10
units =[['km', 'miles', 'league'],['kg', 'pound', 'stone']]
#a. 
print(units[0])
#b. 
print(units[-1] or units[1])
#c. 
print(units[0][0])
#d. 
print(units[1][0])
#e. 
print(units[0][1:])
#f. 
print(units[1][0:2])

#bai11
units =[['km', 'miles', 'league'],['kg', 'pound', 'stone']]
#a.
print(units[-2])
#b. 
print(units[-1])
#c. 
print(units[-2][-3])
#d. 
print(units[-1][-3])
#e. 
print(units[-2][-2:])
#f. 
print(units[-1][:-1])
