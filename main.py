        
class Grading():
    perfomance = {}
    perfomance_out = {}
    

    def __init__(self,math,eng ,kis ,sci ,sos ):
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
        self.perfomance["total"] = self.total
        self.perfomance["avarage_mks"] =self.avg_marks
        self.perfomance["grade"] = self.grade
        self.perfomance_out[name] = self.perfomance
       


results = {}
subject = {}
subject_out = {}
for i in range(0,int(input("Enter no of students: "))):
    name = input("Enter name \n")
    marks = [int(input("Mathematics: ")),
        int(input("English: ")),
        int(input("Kiswahili: ")),
        int(input("Science: ")),
        int(input("Social Studies: "))]
    results[name] = marks
    Grading(*results[name])
    s = Grading
    subject["maths"] = marks[0]
    subject["eng"] = marks[1]
    subject["kis"] = marks[2]
    subject["sci"] = marks[3]
    subject["sos"] = marks[4]
    subject_out[name] = subject
print(subject_out)
print(s.perfomance_out)





    


        
       
    




    