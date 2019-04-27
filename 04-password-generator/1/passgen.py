
import string
import random

def _generate(length):
    pw = []
    for _ in range(0, length):
        c = random.choice(string.ascii_lowercase)
        pw.append(c)
    return ''.join(pw)

def main():
    password = _generate(20)
    print(password)

if __name__ == '__main__':
    main()
