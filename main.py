print ('Hello to My Calucaltor, Lets Start')
num1 = input("Enter First Number:\n")
operator = input("Select which operator you need(+, -, *, /,**):\n")
num2 = input("Enter Second Number:\n")

num1 = float(num1)
num2 = float(num2)

out = None

if operator == "+":
    out =  num1 + num2
elif operator == "-":
    out = num1 - num2
elif operator == "*":
    out = num1 * num2
elif operator == "/":
    out = num1 / num2
elif operator == "**":
    out = num1 ** num2
print("Answer: " + str(out))

