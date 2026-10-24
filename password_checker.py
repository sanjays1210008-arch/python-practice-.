def check_password(password):
    if len(password)<8:
        return False
    upper=False
    lower=False
    digit=False
    special=False
    for ch in password:
        if ch.isupper():
            return True
        elif ch.islower():
            return True
        elif ch.isdigit:
            return True
        else:
            return True
    return uppper and lower and digit and special
print(check_password("Hello@131"))