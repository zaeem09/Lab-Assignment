num = int(input("Enter any number: "))
fact=1
if num < 0:
    print("Factorial of Negative Number cannot be given")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact*=i
print("The factorial of ", num, "is", fact)
