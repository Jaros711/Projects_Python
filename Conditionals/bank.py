answer = input("Give me your greeting: ").strip().lower()

if answer.startswith("hello"):
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")

