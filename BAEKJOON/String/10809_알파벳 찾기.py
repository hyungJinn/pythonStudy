s = input()
alphabet = list(range(97, 123))

for x in alphabet:
    print(s.find(chr(x)), end = " ")