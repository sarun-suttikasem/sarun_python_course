name = input("Enter your name: ")
letters = list(name)

a = letters.count('a')
A = letters.count('A')
e = letters.count('e')
E = letters.count('E')
i = letters.count('i')
I = letters.count('I')
o = letters.count('o')
O = letters.count('O')
u = letters.count('u')
U = letters.count('U')

vowels = a + A + e + E + i + I + o + O + u + U

print(f"You have {vowels} vowels")
