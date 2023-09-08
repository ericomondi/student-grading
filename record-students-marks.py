# def student_names():
#     names = []
#     for i in range(0,int(input("Enter no of students: "))):
#         name = input("Enter name \n")
#         names.append(name)
#     print(names)
# student_names()

# results = []

# for i in range(0,int(input("Enter no of students: "))):
#     marks = [int(input("Mathematics: ")),
#             int(input("English: ")),
#             int(input("Kiswahili: ")),
#             int(input("Science: ")),
#             int(input("Social Studies: "))]
#     # results.append(marks)

# # print(results)

results = {}

for i in range(0,int(input("Enter no of students: "))):
    name = input("Enter name \n")
    marks = [int(input("Mathematics: ")),
            int(input("English: ")),
            int(input("Kiswahili: ")),
            int(input("Science: ")),
            int(input("Social Studies: "))]
    results[name] = marks

# print(results)



    




