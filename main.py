        
class Grading():
    perfomance = {}
    perfomance_out = {}
    out = []
    

    def __init__(self,name,math,eng ,kis ,sci ,sos ):
        self.name = name
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
        self.perfomance_out[self.name] = self.perfomance
        self.out.append(self.perfomance_out)
       


results = []
subject = []
# subject_out = {}
for i in range(0,int(input("Enter no of students: "))):
    
    inputs = [input("Enter name \n"),
        int(input("Mathematics: ")),
        int(input("English: ")),
        int(input("Kiswahili: ")),
        int(input("Science: ")),
        int(input("Social Studies: "))]
    results.append(inputs)

for i in results:
    Grading(*results[i])
    
s = Grading
print(results)
print(s.out)
    




    


        
       
    




    