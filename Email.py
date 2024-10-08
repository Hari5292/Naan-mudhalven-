email = input("Enter Your Email: ").strip()

username = email[:email.index('@')]
domain = email[:email.index('@') + 100:]

print(f"Your username is {username} & domain is {domain}")

phone number = input(" Enter your phone number:").strip()

