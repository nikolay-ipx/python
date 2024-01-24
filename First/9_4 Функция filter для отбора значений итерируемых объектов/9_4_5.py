from string import ascii_lowercase, ascii_uppercase

correct_chars = ascii_lowercase + ascii_uppercase + '1234567890_.@'


def email_check(email):
    if email.count('@') != 1 or email.count('.') != 1:
        return False
    elif email.index('.') < email.index('@'):
        return False

    for i in email:
        if i not in correct_chars:
            return False

    return True


emails = input().split()
print(*list(filter(email_check, emails)))