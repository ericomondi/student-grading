# the program promts you to enter a students name and score per subject
# then outputs a dictionary containing the name as the key and (total, avarage marks, and grade)
# as key values in a dictionary

class Students():
    stud_names = []
    # stud_name = ""

    def __init__(self, name = input("Enter name. \n")):
        self.name = name
        self.add()
    
    
    def add(self):
        self.stud_names.append(self.name)
        

class Grading(Students):
    perfomance = {}
    results = {}
    
    def __init__(
            self,
            math = int(input("Mathematics: ")),
            eng = int(input("English: ")),
            kis = int(input("Kiswahili: ")),
            sci = int(input("Science: ")),
            sos = int(input("Social Studies: "))

     ):
        self.math = math
        self.eng = eng
        self.kis = kis
        self.sci = sci
        self.sos = sos
        self.find_total_marks()
        self.find_avg_marks()
        self.find_grade()
        self.insert_results()

    def find_total_marks(self):
        self.total = self.math + self.eng + self.kis + self.sci + self.sos
        # print(f'The total is {self.total}')
       
    def find_avg_marks(self):
        self.avg_marks = self.total / 5
        # print(f'The avarage marks is {self.avg_marks}')
       
    def find_grade(self):
        if self.avg_marks > 79:
            self.grade = "A"
        elif self.avg_marks >= 60 and self.avg_marks <= 79:
            self.grade = "B"
        elif self.avg_marks > 49 and self.avg_marks <= 59:
            self.grade = "C"
        elif self.avg_marks >= 40 and self.avg_marks <= 49:
            self.grade = "D"
        else:
            self.grade = "E"
        # print(f'The grade is {self.grade}')
       
    def insert_results(self):
        self.perfomance["total"] = self.total
        self.perfomance["avarage_mks"] =self.avg_marks
        self.perfomance["grade"] = self.grade
        self.results[self.stud_names[0]] = self.perfomance
        print(self.results)
        
        

Students() 

Grading()

    


        

        


