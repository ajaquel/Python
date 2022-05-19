exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))

overall_grade = (exam1_grade + exam2_grade + exam3_grade) / 3

print('Your overall grade is:', overall_grade)



#Calculates the overall grade for four equally-weighted programming assignments,
# where each assignment is graded out of 50 points. Hint: First calculate the percentage
# for each assignment (e.g., score / 50), then calculate the overall grade percentage
# (be sure to multiply the result by 100).

exam1_grade = float(input('Enter score on Exam 1 (out of 50):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 50):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50):\n'))

overall_grade = (((exam1_grade / 50) + (exam2_grade / 50) + (exam3_grade / 50) + (exam4_grade / 50)) / 4) * 100

print('Your overall grade is:', overall_grade)



#Calculates the overall grade for four equally-weighted programming assignments,
# where assignments 1 and 2 are graded out of 50 points and assignments 3 and 4 are graded out of 75 points.


exam1_grade = float(input('Enter score on Exam 1 (out of 50):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 50):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 75):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 75):\n'))

overall_grade = (((exam1_grade / 50) + (exam2_grade / 50) + (exam3_grade / 75) + (exam4_grade / 75)) / 4) * 100

print('Your overall grade is:', overall_grade)





#Calculates the overall grade for a course with three equally-weighted exams (graded out of 100)
# that account for 60% of the overall grade and four equally-weighted programming assignments
# (graded out of 50) that account for 40% of the overall graded. Hint: The overall grade can
# be calculated as 0.6 * averageExamScore + 0.4 * averageProgScore.


exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))
exam4_grade = float(input('Enter score on Exam 4 (out of 50):\n'))
exam5_grade = float(input('Enter score on Exam 5 (out of 50):\n'))
exam6_grade = float(input('Enter score on Exam 6 (out of 50):\n'))
exam7_grade = float(input('Enter score on Exam 7 (out of 50):\n'))

#overall_grade = (((exam1_grade / 50) + (exam2_grade / 50) + (exam3_grade / 75) + (exam4_grade / 75)) / 4) * 100

avg_exam_score: float = (((exam1_grade) + (exam2_grade) + (exam3_grade)) / 3) * 100
avg_prog_score: float = (((exam4_grade / 50) + (exam5_grade / 50) + (exam6_grade / 50) + (exam7_grade / 50)) / 4) * 100

overall_grade = avg_exam_score * 0.6 + avg_prog_score * 0.4

print('Your overall grade is:', overall_grade)


#Extend the program to support the grading scheme for one (or all) of the courses.

