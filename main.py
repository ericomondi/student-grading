class Grading():
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
        self.insert_dict()

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
       
    def insert_dict(self):
        self.results["total"] = self.total
        self.results["avarage_mks"] =self.avg_marks
        self.results["grade"] = self.grade

class Students(Grading):
    stud_result = {}
    
    def __init__(self, name = input("Enter name: ")):
        self.name = name
        self.identity()

    def identity(self):
        self.stud_result[self.name]= self.results
        print(self.stud_result)

Grading() 
Students()

        

        


