print("Hello, I am FeelingBot. What is your name?")
name = input()

print(f"Nice to meet you, {name}")

print(f"How are you doing {name}? (Good, Bad, Excited, Scared)")
feeling = input().lower()

if feeling == "good":
    print("It's great that you are feeling good today!")
    print(f"Have a good day, {name}! Goodbye, see you soon!")
elif feeling == "bad":
    print("I hope that you feel better soon!")
    print(f"I hope your day gets better, {name}! Goodbye, see you soon!")
elif feeling == "excited":
    print("It's great that you are excited!")
    response = input("What is making you feel excited? or 'I'm not sure' ")
    response = response.lower()
    if response == "i'm not sure":
        print("That's okay. Sometimes you're excited and you don't know why.")
    else:
        print(f"I'm happy that you're excited for {response}")
    print(f"Have a good day, {name}! Goodbye, see you soon!")
elif feeling == "scared":
    print("I'm sorry that you're scared.")
    response = input("What is making you feel scared? or 'I'm not sure' ")
    response = response.lower()

    if response == "i'm not sure":
        print("That's okay. Sometimes you're scared and you don't know why.")
    else:
        print(f"I'm sorry that you're scared for {response}")

    print(f"I hope your day gets better, {name}! Goodbye, see you soon!")
else:
    print("I understand. Sometimes it's hard to put your emotions into words.")