#  the program prompts the user to enter the no of students, name
# and score per-subject then outputs a dictionary with the students
#  names as the key and the scores per subject as a the key-value in a list 

results = {}

for i in range(0,int(input("Enter no of students: "))):
    name = input("Enter name \n")
    marks = [int(input("Mathematics: ")),
            int(input("English: ")),
            int(input("Kiswahili: ")),
            int(input("Science: ")),
            int(input("Social Studies: "))]
    results[name] = marks

print(results)





    




