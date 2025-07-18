def main():
    text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    converted = text.lower().strip()
    match converted:
        case "42":
            print("Yes")
        case "forty-two":
            print("Yes")
        case "forty two":
            print("Yes")
        case "Forty-Two":
            print("Yes")
        case _:
            print("No")
main()

