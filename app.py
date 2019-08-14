#PART 1

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
    def add_skill(self, newSkill):
        self.skills.append(newSkill)
        print(f"{self.name} added {newSkill} to her skillset")

       

ben = Student("ben", "I want to make a website!")
sally = Student("sally", "I want to make an app!")
# print("name: ", ben.name, " | reason: ", ben.reasonToAttend)

alice = Instructor("alice", "I've been coding in Python for 5 years and wanted to share what i love!", ["Python", "Javascript", "C++"])
print("name: ", alice.name, " | reason: ", alice.bio," | skills: ", alice.skills)

# alice.hello()
alice.add_skill("skateboarding")
alice.add_skill("lazertag")
print(alice.skills)

# print(ben.__class__)


class Workshop():
    def __init__(self, subject="", date="", participants=[], instructors=[]):
        self.subject = subject
        self.date = date
        self.participants = participants
        self.instructors = instructors
    def add_participant(self, addedperson):
        if isinstance(addedperson, Student):
            self.participants.append(addedperson)
            print(f"{addedperson.name} was added to the class as a participant")
        elif isinstance(addedperson, Instructor):
            self.instructors.append(addedperson)
            print(f"{addedperson.name} was added to the class as an instructors")    

intro_to_dev = Workshop("development", "march 1st, 2020")

intro_to_dev.add_participant(ben)
intro_to_dev.add_participant(sally)
intro_to_dev.add_participant(alice)


