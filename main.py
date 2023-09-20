        
class Grading():
    # perfomance = {}
   
    
    def __init__(self,name,math,eng ,kis ,sci ,sos ):
        self.name = name
        self.math = math
        self.eng = eng
        self.kis = kis
        self.sci = sci
        self.sos = sos
        self.subject = {}
        self.perfomance = {}
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
        self.subject["name"] = self.name
        self.subject["maths"] = self.math
        self.subject["english"] = self.eng
        self.subject["kiswahili"] = self.kis
        self.subject["science"] = self.sci
        self.subject["sosial-studies"] = self.sos
        
        self.perfomance["name"] = self.name
        self.perfomance["total"] = self.total
        self.perfomance["avarage_mks"] =self.avg_marks
        self.perfomance["grade"] = self.grade

        
        
       
results = []
perfomance_out = []
subject_out = []

for i in range(1,int(input("Enter no of students: "))+ 1):
    
    inputs = [input("Enter name \n"),
        int(input("Mathematics: ")),
        int(input("English: ")),
        int(input("Kiswahili: ")),
        int(input("Science: ")),
        int(input("Social Studies: "))]
    results.append(inputs)

for result in results:
    s = Grading(*result)
    subject_out.append(s.subject)
    perfomance_out.append(s.perfomance)

    

print(subject_out)
print(perfomance_out)   




    


        
       
    




    