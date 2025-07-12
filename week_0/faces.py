def main():
    text_input = input()
    convert(text_input)

def convert(text):
    print(text.replace(":)", "🙂").replace(":(", "🙁"))

main()