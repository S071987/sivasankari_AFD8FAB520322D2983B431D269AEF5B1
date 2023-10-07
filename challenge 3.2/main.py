class student:

  def __init__(self, name, roll_number,cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list,
                         key =lambda student:student.cgpa,
                         reverse= True)
  return sorted_students


students=[student("pooja","A123",9.2),
          student("siva","B234",9.4),
          student("sri","c789",8.6),
          student("sathya","d678",9.0)]

sorted_students = sort_students(students)

for student in sorted_students:
  print("name: {}, Roll Number: {}, cgpa:{}".format(student.name,student.roll_number,
                                                    student.cgpa))


