a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Valid Triangle")
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    elif (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
        print("Right Angled Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid Triangle")
