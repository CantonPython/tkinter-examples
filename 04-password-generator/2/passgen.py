
import string
import random

def _generate(length, upper=0, digits=0, symbols=0):
    pw = []
    for _ in range(upper):
        c = random.choice(string.ascii_uppercase)
        pw.append(c)
    for _ in range(digits):
        c = random.choice(string.digits)
        pw.append(c)
    for _ in range(symbols):
        c = random.choice(string.punctuation)
        pw.append(c)
    length = length - len(pw)
    for _ in range(length):
        c = random.choice(string.ascii_lowercase)
        pw.append(c)
    random.shuffle(pw)
    return ''.join(pw)

def main():
    password = _generate(20, upper=1, digits=2, symbols=3)
    print(password)

if __name__ == '__main__':
    main()
