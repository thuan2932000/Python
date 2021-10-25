class Student:
    def __init__(self, member_string:str, student_number:int, courses_taken:str, courses_taking: str):
        self.member_string = member_string
        self.student_number = student_number
        self.courses_taken = courses_taken
        self.courses_taking = courses_taking

    def __str__(self):
        member_string = super().__str__()
        return '''{}\n{}\nPrevious courses: {}\nCurrent courses:{}'''.format(member_string,self.student_number,self.courses_taken,self.courses_taking)

    def __repr__(self):
        return "Student('{}', '{}', [{}], [{}])".format(
 self.member_string, self.student_number,
 ','.join(self.courses_taken), ','.join(self.courses_taking))

class Member:
    def __init__(self, name:str, address:str, email:str):
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):
        return "Member('{}', '{}', '{}')".format(self.name, self.address, self.email)

class Faculty:
    def __init__(self, name:str, address:str, email:str, faculty_number:int, courses_teaching: str):
        self.name = name
        self.address = address
        self.email = email
        self.faculty_number = faculty_number
        self.courses_teaching = courses_teaching

    def __repr__(self):
        return "Faculty('{}', '{}', '{}', {}, [{}])".format(
 self.name, self.address, self.email, self.faculty_number,
 ','.join(self.courses_teaching))

student = Student('Paul', 'Ajax', 'pgries@cs.toronto.edu','1234')
member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu','1234', '[]')

print(student.__str__())
print(member.__repr__())
print(faculty.__repr__())
print(student.__repr__())