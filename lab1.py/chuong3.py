#bai 1
a = min(2, 3, 4)
b = max(2, -3, 4, 7, -5)
c = max(2, -3, min(4, 7), -5)
print(a,b,c)
#bai 2
a1 = min(max(3, 4), abs(-5))
b1 = abs(min(4, 6, max(2, 8)))
c1 = round(max(5.572, 3.258), abs(-2))
print(a1,b1,c1)
#bai 3 
def triple(num):
    return num * 3
print(triple(3))
#bai 4
def absolute_difference(number1, number2):
    return abs(number1 - number2)
print(abs(20-40))
#bai 5
def km_to_miles(km):
    return km/1.6
print(km_to_miles(50))
#bai 6
def average_grade(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3
print(average_grade(20,5,95))
#bai 7 
def top_three_avg(grade1, grade2, grade3, grade4):
    total = grade1 + grade2 + grade3 + grade4
    top_three = total - min(grade1, grade2, grade3, grade4)
    #return top_three / 3
    """return max(average_grade(grade1, grade2, grade3),
    average_grade(grade1, grade2, grade4),
    average_grade(grade1, grade3, grade4),
    average_grade(grade2, grade3, grade4))"""
    return (grade1 + grade2 + grade3) / 3
print(top_three_avg(30,40,50,60))
#bai 8 
def weeks_elapsed(day1, day2):
    return int(abs((day1 - day2) / 7))
print(weeks_elapsed(3,20))
print(weeks_elapsed(20,3))
print(weeks_elapsed(8,5))
print(weeks_elapsed(40,61))

#bai 9
def square(num):                       
    num = num * 3
    return num 
print(square(3))          






    





