#bai1 
filename = input('Which file would you like to back-up? ')
new_filename = filename + '.bak'
backup = open(new_filename, 'w')
for line in open(filename):
 backup.write(line)
 backup.close()

