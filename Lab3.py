a, b = str(input("Please enter number of x and y")).split()
op = input('Operater input + - * /')
x = float(a)
y = float(b)
result = {
    "+":lambda x, y:x+y,
    "-":lambda x, y:x-y,
    "*":lambda x, y:x*y,
    "/":lambda x, y:x/y,
}
print(result[op](x,y))