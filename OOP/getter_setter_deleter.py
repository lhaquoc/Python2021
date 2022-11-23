class Student:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten

    @property
    def email(self):
        return f'{self.ho}-{self.ten}@name.com'

    @property
    def ho_ten(self):
        return f'{self.ho} {self.ten}'

    @ho_ten.setter
    def ho_ten(self, ho_ten):
        ho, ten = ho_ten.split(' ')
        self.ho = ho
        self.ten = ten

    @ho_ten.deleter
    def ho_ten(self):
        self.ho = None
        self.ten = None
        print('Da xoa ho va ten')


stu_A = Student("Le", "Hai")
stu_A.ho_ten = "Le Hai"
print(stu_A.ho_ten)
del stu_A.ho_ten

print(stu_A.ho)
print(stu_A.ten)
