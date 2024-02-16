"""
Problem statement:
Multiple Select Questions (MSQ) could have more than one correct answers. The marks scored by a student in a MSQ will be determined by the following conditions:
(1) If the question has 
c correct options, each individual correct option carries n/c marks.
(2) If a student selects any of the wrong options, the marks awarded for the question will be 0.
Calculate the marks obtained by the student and print this as float value.
The input contains four lines.
(1) First line is the number of marks for the question.
(2) Second line contains the number of options for the question.
(3) Third line is a comma-separated sequence of correct options for this question.
(4) Fourth line is a comma-separated sequence of options given by the student.
Write a program to print the number of marks scored by a student.
Note: Options are numbered using positive integers in the range [1,9], endpoints inclusive. A question will have at most nine options. 
The number of marks and the correct options will always be integers.
"""

marks = int(input())
options = int(input())
correct = list(map(int, input().split(',')))
selected = list(map(int, input().split(',')))
pq = marks / len(correct)
m = 0
for i in selected:
    if i in correct:
        m += pq
    else:
        m = 0.0
        break
print(m)
