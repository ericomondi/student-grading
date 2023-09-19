import random


class Grading():
    
    def __init__(self,name,math,eng ,kis ,sci ,sos ):
        self.name = name
        self.math = math
        self.eng = eng
        self.kis = kis
        self.sci = sci
        self.sos = sos
        self.performance = {} # This is specific to each instance
        self.find_total_marks()
        self.find_avg_marks()
        self.find_grade()
        self.insert_results()
        

    def find_total_marks(self):
        self.total = self.math + self.eng + self.kis + self.sci + self.sos
        
        
       
    def find_avg_marks(self):
        self.avg_marks = self.total / 5
        
        
       
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
       

    def insert_results(self):
        self.performance["name"] = self.name
        self.performance["total"] = self.total
        self.performance["avarage_mks"] =self.avg_marks
        self.performance["grade"] = self.grade

results = []
performance_out = []
student_names = ['Student A', 'Student B', 'Student C']
student_marks = [[random.randint(1, 100) for x in range(1,6)] for _ in range(len(student_names))]


for name, marks in zip(student_names, student_marks):
    results.append([name, *marks]) 
    s = Grading(*[name, *marks])
    print(s.performance)
    performance_out.append(s.performance)

for result in results:
    print(result)

for performance in performance_out:
    print(performance) 