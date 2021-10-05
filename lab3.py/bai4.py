def process_file(reader):
# Find and print the first piece of data.
    line = skip_header(reader).strip()
    print(line)

# Read the rest of the data.
    print(reader.read('alkline_metals.txt'))