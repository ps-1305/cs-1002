"""
Problem statement:
Take a number and confirm that it satisfies the following conditions
(1) The number should start with one of these digits: 6, 7, 8, 9
(2) The number should be exactly 10 digits long.
(3) No digit should appear more than 7 times in the number.
(4) No digit should appear more than 5 times in a row in the number.
If the fourth condition is not very clear, then consider this example: the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string valid if the phone number is valid. If not, print the string invalid.
"""


number = input()
if number[0] in "6789" and len(number) == 10:
    for i in range(10):
        if number.count(str(i)) <= 7 and str(i)*6 not in number and str(i)*7 not in number and str(i)*8 not in number and str(i)*9 not in number and str(i)*10 not in number:
            pass
        else:
            print("invalid")
            exit()
    
    print("valid")
else:
    print("invalid")
