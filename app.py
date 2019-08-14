class Member():
    def __init__(self, name=""):
        self.name = name
    def hello(self):
        print(f"Hi, my name is {self.name}")

class Student(Member):
    def __init__(self, name="", reasonToAttend=""):
        Member. __init__ (self)
        self.name = name
        self.reasonToAttend = reasonToAttend   

class Instructor(Member):
    def __init__(self, name="", bio="", skills=[""]):
        Member. __init__ (self)
        self.name = name
        self.bio = bio
        self.skills = skills
    def addSkill(self, newSkill):
        self.skills = self.skills + newSkill
        print(f"{self.name} added {self.skills}")

       

    
ben = Student("ben", "I've been coding in Python for 5 years and want to share the love!")
print("name: ", ben.name, " | reason: ", ben.reasonToAttend)

alice = Instructor("alice", "I've been coding in Python for 5 years and wanted to share what i love!", ["Python", "Javascript", "C++"])
print("name: ", alice.name, " | reason: ", alice.bio," | skills: ", alice.skills)

alice.hello()
alice.addSkill(["skateboarding", "underwater basket weaving"])
print(alice.skills)

