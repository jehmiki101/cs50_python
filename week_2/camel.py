def main():
    text_camelcase = input("camelCase: ")
    snake_case(text_camelcase)

def snake_case(text):
    letter = list(text)
    for _ in list(text):
        if _.isupper():
            print("_" + _.lower(), end="")
            continue
        print(_, end="")

main()
