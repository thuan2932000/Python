def read_molecule(reader):
# If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

    if not (line.startswith('CMNT') or line.isspace()):
# Name of the molecule: "COMPND name"
        key, name = line.split()

# Other lines are either "END" or "ATOM num atom_type x y z"
        molecule = [name]
    else:
        molecule = None

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            key, num, atom_type, x, y, z = line.split()
            if molecule == None:
                molecule = []
                molecule.append([atom_type, x, y, z])

    return molecule