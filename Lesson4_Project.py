def FactorialCalculator(Num):
    if Num <= 0:
        return None
    Multiply = 1
    for x in range(1, Num+1):
        Multiply = Multiply * x
    return Multiply
    
print("Your number factorial is: ")
print(FactorialCalculator(-2))