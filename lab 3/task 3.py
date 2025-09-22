marks=int(input("Enter your marks(0-100):"))

if marks>=90:
    grade="A"
    print(grade)

elif marks>=75 and marks<90: #'and' ensures both conditions are true
    grade="B"
    print(grade)

elif marks>=50 and marks<75:
    grade="C"
    print(grade)

else: #marks<50
    grade="F"
    print(grade)


