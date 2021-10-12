def read_molecule(reader):
# If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

# Name of the molecule: "COMPND name"
    key, name = line.split()

# Other lines are either "END" or "ATOM num atom_type x y z"
molecule = [name]
reading = True

serial_number = 1
while reading:
    line = reader.readline()
    if line.startswith('END'):
        reading = False
    else:
        key, num, atom_type, x, y, z = line.split()
        if int(num) != serial_number:
            print('Expected serial number {0}, but got {1}'.format(serial_number, num))
    molecule.append([atom_type, x, y, z])
    serial_number += 1
        
 return molecule