def main():
    expression_input = input("Expression: ").strip().split()
    x = int(expression_input[0])
    y = int(expression_input[2])
    if expression_input[1] == "+":
        print(float(x + y))
    elif expression_input[1] == "-":
        print(float(x - y))
    elif expression_input [1] == "*":
        print(float(x * y))
    elif expression_input[1] == "/":
        print(float(x / y))



main()