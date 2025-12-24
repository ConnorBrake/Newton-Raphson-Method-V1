import math

org_function = input("Input a Function: ")
der_function = input("Input the Function's Derivative: ")
precise = float(input("How Precise Should the Output Be (in decimals): "))
x = float(input("Input a Starting X Value: "))

def org_function_to_maths():
    return eval(org_function)

def der_function_to_maths():
    return eval(der_function)

def Newton_Raphson_Method(x):
    x = x - (org_function_to_maths() / der_function_to_maths())
    return x

for i in range(0, 100):
    prev_x = x
    x = Newton_Raphson_Method(x)
    if(prev_x == round(x - precise)):
        break

print(x)
print("Rounded: " + str(round(x)))