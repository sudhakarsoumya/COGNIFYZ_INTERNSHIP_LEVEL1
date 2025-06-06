import re
def is_valid_email(email):
    email_regex=re.compile(r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    if email_regex.match(email):
        return True
    else:
        return False
while True:
    email=input("Enter an email address to validate:").strip()
    if is_valid_email(email):
        print(f"'{email}' is a valid email address")
    else:
        print(f"'{email}' is not a valid email address")
    continue_choice=input("want to validate another email address ? (yes to continue, no to exit):").strip().lower()
    if continue_choice!="yes":
        print("Exiting the email validator.......goodbye!")
        break