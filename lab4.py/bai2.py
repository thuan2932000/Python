# Cau 2: 
# Read file multimol.pdb. Return the first item is the name of compound
# then list contains type, coordinates of that atom 
def read_molecule(reader):
    # Nếu không có dòng nào thì kết thúc
    line = reader.readline()
    if not line:
        return None
    # Compound name
    key, name = line.split()

    molecule = [name]
    line = reader.readline()
    
    # the atoms in the molecule.
    while not line.startswith('END'):
        key, num, atom_type, x, y, z = line.split()
        molecule.append([atom_type, x, y, z])
        line = reader.readline()
    return molecule

def read_all_molecules(reader):
    result = []
    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: 
            result.append(molecule)
        else:
            reading = False
    return result
if __name__ == "__main__":
    molecule_file = open('D:/multimol.txt','r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)