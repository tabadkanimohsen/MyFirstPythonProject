def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "تقسیم بر صفر امکان‌پذیر نیست"

print("ماشین حساب ساده")
num1 = float(input("عدد اول: "))
num2 = float(input("عدد دوم: "))
op = input("عملگر (+, -, *, /): ")

if op == "+":
    print("نتیجه:", add(num1, num2))
elif op == "-":
    print("نتیجه:", subtract(num1, num2))
elif op == "*":
    print("نتیجه:", multiply(num1, num2))
elif op == "/":
    print("نتیجه:", divide(num1, num2))
else:
    print("عملگر نامعتبر")
