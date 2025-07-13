def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    remaining = d[1:]
    converted  = float(remaining)
    return converted

def percent_to_float(p):
    remaining = p[:-1]
    converted_int = int(remaining)
    converted_float = float(converted_int / 100)
    return converted_float

main()