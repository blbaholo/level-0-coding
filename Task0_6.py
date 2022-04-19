def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    if num2> num1 and num2>num3:
        return num2
    if num3>num1 and num3>num2:
        return num3
    if num1==num2 and num1>num3:
        return "It's a tie!"
    if num1==num3 and num1>num2:
        return "It's a tie!"
    if num2==num3 and num2>num1:
        return "It's a tie!"
    if num1==num2==num3:
        return "It's a tie"
print(maximum(4,4,3))
