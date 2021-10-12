# Cau 3: Return a set of tuples where each tuple contains a male from males and a female from females.
def mating_pairs(males, females):
    """ >>> mating_pairs({'Anne', 'Beatrice', 'Cari'}, {'Ali', 'Bob', 
    'Chen'})
    {('Cari', 'Chen'), ('Beatrice', 'Bob'), ('Anne', 'Ali')}
    """
    try:
        pairs = set()
        num_gerbils = len(males)
        for i in range(num_gerbils):
            male = males.pop()
            female = females.pop()
            pairs.add((male, female),)
        return pairs
    except:
        return print("Loi!!! Số lượng Males và Females phải bằng nhau")
males = {'Nam1', 'Nam2', 'Nam3'}
females = {'Nu1', 'Nu2', 'Nu3'}
mating_pairs(males, females)