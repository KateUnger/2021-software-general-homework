Test1Score = float(input("Test 1 Score: "))
Test2Score = float(input("Test 2 Score: "))
Test3Score = float(input("Test 3 Score: "))
Average = (Test1Score + Test2Score + Test3Score)/3
print("Average: ")
print(Average)
if Average >= 90:
    print("Your grade is an A.")
elif Average < 90 and Average >= 80:
    print("Your grade is a B.")
elif Average < 80 and Average >= 70:
    print("Your grade is a C.")
elif Average < 70 and Average >= 60:
    print("Your grade is a D")
else:
    print("Your letter grade is F, you have failed.")