class Person:

    def __init__(self):
        self.name = 'Zakhele Ndlovu'
        self.age = 24
        self.qualification = 'Marketing Management'
        self.languages_spoken = ['IsiZulu','English','IsiXhosa','Pedi','Setswana','Swati']

    def getName(self):
        name=self.name
        print(name)

    def getAge(self):
        age = self.age
        print(age)

    def getQualification(self):
        qual = self.qualification
        print(qual)

    def getLaguagesSpoken(self):
        ls = self.languages_spoken
        print(ls)

    def thankYou(self):
        print('Thanks for dropping by :)')

a = Person()
a.getAge()
a.getName()
a.getQualification()
a.getLaguagesSpoken()
a.thankYou()