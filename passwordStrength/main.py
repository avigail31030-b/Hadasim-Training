from collections import Counter

def is_strong_password(password):
    if not len(password) >= 8:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(not c.isalnum() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if has_three_consecutive_chars(password):
        return False
    if any(count > 2 for count in Counter(password).values()):
        return False
    return True
  
def has_three_consecutive_chars(password):
    for i in range(len(password) - 2):
        a = password[i]
        b = password[i + 1]
        c = password[i +2]
        if is_consecutive_triple(a, b, c):
            return True
    return False


def is_consecutive_triple(a, b, c):
    return ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1

if __name__ == "__main__":
    password = input("Enter password: ")
    print(is_strong_password(password))  
