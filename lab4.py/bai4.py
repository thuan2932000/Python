# Cau 4: Return a list of the authors in PDB files names appear in filenames.
def get_authors(filenames):
    authors = set()
    for filename in filenames:
        for line in open(filename,'r'):
            if line.lower().startswith('author'):
                author = line[6:].strip()
                authors.add(author)
    return authors
if __name__ == "__main__":
    list_file = ['D:/PDB_1.txt','D:/PDB_2.txt']
    print(get_authors(list_file))