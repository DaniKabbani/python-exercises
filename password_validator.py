SPECIAL_CHARACTERS = "!@#$%^&*()-_=+[]{};:,.?/"
MIN_LENGTH = 8


def check_password(password):
    """Return a list of the rules the password fails (empty if it is valid)."""
    problems = []
    if len(password) < MIN_LENGTH:
        problems.append(f"at least {MIN_LENGTH} characters")
    if not any(c.isupper() for c in password):
        problems.append("an uppercase letter")
    if not any(c.islower() for c in password):
        problems.append("a lowercase letter")
    if not any(c.isdigit() for c in password):
        problems.append("a number")
    if not any(c in SPECIAL_CHARACTERS for c in password):
        problems.append(f"a special character ({SPECIAL_CHARACTERS})")
    return problems


if __name__ == "__main__":
    while True:
        problems = check_password(input("Enter your password: "))
        if not problems:
            print("Password is valid.")
            break
        print("Password is invalid. It needs:")
        for problem in problems:
            print(f"  - {problem}")
