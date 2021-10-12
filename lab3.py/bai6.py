import time_series

def smallest_value_skip(reader):
    line = time_series.skip_header(reader).strip()

# Now line contains the first data value; this is also the smallest value
# found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line == '-':
            continue

    value = int(line)
    smallest = min(smallest, value)

    return smallest

if __name__ == '__main__':
    with open('hebron.txt', 'r') as input_file:
        print(smallest_value_skip(input_file))