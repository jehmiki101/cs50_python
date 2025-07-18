def main():
    greeting = input("Greeting: ").lower().strip()
    if hello(greeting) == True:
        print("$0")
    else:
        converted(greeting)

def hello(gr):
    hello = "hello"
    return(hello in gr)


def converted(gr):
    remaining = gr[0]
    if remaining == "h":
        print("$20")
    else:
        print("$100")

main()
