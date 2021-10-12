# Cau 8:  return True if they represent a balanced color.
def is_balanced(color_to_factor):
    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0
is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})